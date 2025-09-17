from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete
from models.auth_models import Projetos, Tags
from dependencies import get_session
from schemas.auth_schemas import ProjetosSchemas, ProjetosSchemasCadastrar
from sqlalchemy.orm import Session

project_routes = APIRouter(prefix="/portifolios", tags=["Portifolios"])

@project_routes.post("/cadastrar")
async def cadastrar_portifolio(portifolio_schema:ProjetosSchemasCadastrar, session= Depends(get_session)):
    portifolio = session.query(Projetos).filter(Projetos.titulo==portifolio_schema.titulo).first()
    if portifolio:
        raise(HTTPException(status_code=400, detail="Portifólio já existe."))
    else:
        novo_portifolio = Projetos(portifolio_schema.aluno_id ,portifolio_schema.titulo, portifolio_schema.foto, portifolio_schema.descricao, portifolio_schema.corpo)
        session.add(novo_portifolio)
        for tag_id in portifolio_schema.tags:
            tag = session.query(Tags).filter(Tags.id == tag_id).first()
            if tag:
                novo_portifolio.tags.append(tag)
    session.commit()
    session.refresh(novo_portifolio)
    return {"message": f"Projeto {portifolio_schema.titulo} cadastrado com sucesso!"}
    
@project_routes.get("/listar")
def listar_alunos(session = Depends(get_session)):
    todos_projetos = session.query(Projetos).all()
    if not todos_projetos:
        raise HTTPException(status_code=404, detail="Não há projetos cadastrados.")
    else:
        return [{"id": projeto.id, "titulo": projeto.titulo, "foto": projeto.foto ,"descrição": projeto.descricao, "corpo": projeto.corpo} for projeto in todos_projetos]
        
@project_routes.put("/editar/{projeto_id}")
def editar_portifolio(projeto_id: int, projetos_schema: ProjetosSchemas, session = Depends(get_session)):
    projeto = session.query(Projetos).filter(Projetos.aluno_id == projeto_id).first()
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado.")
    else:
        projeto.titulo = projetos_schema.titulo
        projeto.foto = projetos_schema.foto
        projeto.descricao = projetos_schema.descricao
        projeto.corpo = projetos_schema.corpo
        session.commit()
        return {"message": f"Projeto {projetos_schema.titulo} atualizado com sucesso!"}
    
@project_routes.delete("/excluir/{projeto_id}")
def excluir_projeto(projeto_id: int, session = Depends(get_session)):
    projeto = session.query(Projetos).filter(Projetos.id == projeto_id).first()
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado.")
    else:
        session.delete(projeto)
        session.commit()
        return {"message": f"Projeto {projeto_id} deletada com sucesso!"}
