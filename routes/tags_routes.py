from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import delete
from typing import List
from models.auth_models import Tags, Projetos
from dependencies import get_session
from schemas.auth_schemas import ProjetosSchemas, TagsSchemas
from sqlalchemy.orm import joinedload  #joinedload carrega todas as tags de cada projeto

tags_routes = APIRouter(prefix="/tags", tags=["Tags"])

@tags_routes.post("/cadastrar")
async def criar_tag(tags_schema: TagsSchemas, session = Depends(get_session)):
    tag = session.query(Tags).filter(Tags.nome==tags_schema.nome).first()
    if tag:
        raise(HTTPException(status_code=400, detail="Tag já cadastrada."))
    else:
        nova_tag = Tags(tags_schema.nome)
        session.add(nova_tag)
        session.commit()
        return{"message": f"tag cadastrada com sucesso - {tags_schema.nome}"}
    

@tags_routes.get("/listar")
def mostrar_tags(session = Depends(get_session)):
    todas_tags = session.query(Tags).all()
    if not todas_tags:
       raise HTTPException(status_code=404, detail="Não há tags cadastradas.")
    else: 
        return [{"id": tag.id, "nome": tag.nome} for tag in todas_tags]

@tags_routes.get("/tags/listar_projetos", response_model=List[ProjetosSchemas])
def buscar_projetos_por_tag(tags_id:List[int]=Query(...), session= Depends(get_session)):
    projetos = (session.query(Projetos).options(joinedload(Projetos.tags)).join(Projetos.tags).filter(Tags.id.in_(tags_id)).all())
    if not projetos:
        raise HTTPException(status_code=404, detail="Nenhum projeto encontrado com essas tags")
    return projetos
        
@tags_routes.put("/editar/{tag_id}")
def editar_tag(tag_id: int, tags_schema: TagsSchemas, session = Depends(get_session)):
    tag = session.query(Tags).filter(Tags.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag não encontrada.")
    else:
        tag.nome = tags_schema.nome
        session.commit()
        return {"message": f"Tag {tag_id} atualizada com sucesso", "tag": {"id": tag.id, "nome": tag.nome}}
    
@tags_routes.delete("/excluir/{tags_id}")
def excluir_tag(tag_id: int, session = Depends(get_session)):
    tag = session.query(Tags).filter(Tags.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag não encontrada.")
    else:
        session.delete(tag)
        session.commit()
        return {"message": f"Tag {tag_id} deletada com sucesso!"}
    


