from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from models.auth_models import Student, Project, Tags
from dependencies import get_session
from schemas.auth_schemas import StudentSchemas
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel

students_routes = APIRouter(prefix="/students", tags=["Students"])

class StudentWithProjectResponse(BaseModel):
    id: int
    name: str
    course: str
    cell: str
    avatar: str
    role: str
    latest_project: Optional[dict] = None
    
    class Config:
        from_attributes = True

@students_routes.post("/register")
async def register_student(student_schemas: StudentSchemas, session = Depends(get_session)):
    student = session.query(Student).filter(Student.name==student_schemas.name).first()
    if student:
        raise HTTPException(status_code=400, detail="Student já cadastrado.")
    else:
        new_student = Student(student_schemas.name, student_schemas.course, student_schemas.cell)
        session.add(new_student)
        session.commit()
        return{"message": f"student {student_schemas.name} successfully registered!"}
    
@students_routes.get("/list")
def list_students(
    session = Depends(get_session),
    tags: Optional[List[int]] = Query(None, description="Filter by tag IDs"),
    search: Optional[str] = Query(None, description="Search term for student name or project title")
):
    """
    Lista estudantes com seus projetos mais recentes.
    Permite filtrar por tags e buscar por termo.
    IMPORTANTE: Se tags forem selecionadas, só mostra estudantes que tenham TODAS as tags (100% compatibilidade).
    """
    # Query base para estudantes
    query = session.query(Student)
    
    # Se há filtro por tags, aplicar lógica de 100% compatibilidade
    if tags and len(tags) > 0:
        # Para cada tag selecionada, o estudante deve ter pelo menos um projeto com essa tag
        for tag_id in tags:
            query = query.filter(
                Student.id.in_(
                    session.query(Project.student_id)
                    .join(Project.tags)
                    .filter(Tags.id == tag_id)
                    .subquery()
                )
            )
    
    # Se há termo de busca, filtrar por nome do estudante ou título do projeto
    if search:
        # Fazer join com Project para buscar também nos títulos dos projetos
        query = query.outerjoin(Project).filter(
            (Student.name.ilike(f"%{search}%")) | 
            (Project.title.ilike(f"%{search}%"))
        )
    
    # Executar query e obter estudantes únicos
    students = query.distinct().all()
    
    if not students:
        raise HTTPException(status_code=404, detail="No students found with the specified criteria.")
    
    result = []
    for student in students:
        # Buscar o projeto mais recente do estudante
        latest_project = session.query(Project).options(joinedload(Project.tags)).filter(
            Project.student_id == student.id
        ).order_by(desc(Project.id)).first()
        
        # Gerar avatar baseado no ID do estudante
        avatar_url = f"https://i.pravatar.cc/150?img={student.id}"
        
        # Mapear curso para role/ocupação
        role_mapping = {
            "Ciência da Computação": "Full Stack Developer",
            "Engenharia de Software": "Software Engineer", 
            "Sistemas de Informação": "Systems Analyst",
            "Design Digital": "UI/UX Designer",
            "Análise e Desenvolvimento de Sistemas": "Systems Developer"
        }
        role = role_mapping.get(student.course, "Developer")
        
        student_data = {
            "id": student.id,
            "name": student.name,
            "course": student.course,
            "cell": student.cell,
            "avatar": avatar_url,
            "role": role,
            "latest_project": None
        }
        
        if latest_project:
            project_tags = [{"id": tag.id, "name": tag.name} for tag in latest_project.tags]
            student_data["latest_project"] = {
                "id": latest_project.id,
                "title": latest_project.title,
                "photo": latest_project.photo,
                "description": latest_project.description,
                "body": latest_project.body,
                "tags": project_tags
            }
        
        result.append(student_data)
    
    # Limitar a 9 resultados para o carrossel
    return result[:9]

@students_routes.put("/edit/{student_id}")
def edit_students(student_id: int, student_schemas: StudentSchemas, session=Depends(get_session)):
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="We did not find this student in the system.")
    else:
        student.name = student_schemas.name
        student.course = student_schemas.course
        student.cell = student_schemas.cell
        session.commit()
        return{"message": f"Student {student.name} updated successfully!"}

