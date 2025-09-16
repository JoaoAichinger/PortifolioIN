from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete
from models.auth_models import Aluno
from dependencies import get_session
from schemas.auth_schemas import AlunoSchemas
from sqlalchemy.orm import Session


students_routes =  APIRouter(prefix="/alunos", tags=["Alunos"])

@students_routes.post("/cadastrar")
async def cadastrar_aluno(aluno_schema: AlunoSchemas, session = Depends(get_session)):
    aluno = session.query(Aluno).filter(Aluno.nome==aluno_schema.nome).first()
    if aluno:
        raise HTTPException(status_code=400, detail="Aluno já cadastrado.")
    else:
        novo_aluno = Aluno(aluno_schema.nome, aluno_schema.celular, aluno_schema.curso)
        session.add(novo_aluno)
        session.commit()
        return{"message": f"aluno {aluno_schema.nome} cadastrado com sucesso."}
    
@students_routes.get("/listar")
def listar_alunos(session = Depends(get_session)):
    todos_alunos = session.query(Aluno).all()
    if not todos_alunos:
        raise HTTPException(status_code=404, detail="Não há alunos cadastrados.")
    else:
        return [{"id": aluno.id, "nome": aluno.nome} for aluno in todos_alunos]
    
@students_routes.put("/editar/{aluno_id}")
def editar_alunos(aluno_id: int, aluno_schema: AlunoSchemas, session=Depends(get_session)):
    aluno = Aluno.session.query(Aluno).fliter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Não encontramos este aluno no sistema.")
    else:
        aluno.nome = aluno_schema.nome
        aluno.curso = aluno_schema.curso
        aluno.celular = aluno_schema.celular
        session.commit()
        return{"message": f"Aluno {aluno.nome} atualizado com sucesso!"}
