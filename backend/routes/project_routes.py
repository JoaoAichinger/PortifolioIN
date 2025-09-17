from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete
from models.auth_models import Project, Tags, Student
from dependencies import get_session
from schemas.auth_schemas import ProjectSchemas, ProjectSchemasCadastrar
from sqlalchemy.orm import Session

project_routes = APIRouter(prefix="/project", tags=["Projects"])

@project_routes.post("/register")
async def register_project(project_schema:ProjectSchemasCadastrar, session= Depends(get_session)):
    student = session.query(Student).filter(project_schema.student_id==Student.id).first()
    if not student:
        raise(HTTPException(status_code=400, detail="Student already exists"))
    else:
        new_project = Project(project_schema.student_id ,project_schema.title, project_schema.photo, project_schema.description, project_schema.body)
        session.add(new_project)
        for tag_id in project_schema.tags:
            tag = session.query(Tags).filter(Tags.id == tag_id).first()
            if tag:
                new_project.tags.append(tag)
    session.commit()
    session.refresh(new_project)
    return {"message": f"Project with title {project_schema.title} successfully registered!"}
    
@project_routes.get("/list")
def list_projects(session = Depends(get_session)):
    all_project = session.query(Project).all()
    if not all_project:
        raise HTTPException(status_code=404, detail="There are no registered projects.")
    else:
        return [{"id": project.id, "title": project.title, "photo": project.photo ,"descrição": project.description, "body": project.body} for project in all_project]
        
@project_routes.put("/edit/{project_id}")
def edit_project(project_id: int, project_schema: ProjectSchemas, session = Depends(get_session)):
    project = session.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="project not found.")
    else:
        project.title = project_schema.title
        project.photo = project_schema.photo
        project.description = project_schema.description
        project.body = project_schema.body
        session.commit()
        return {"message": f"Project with title {project_schema.title} successfully edited!"}
    
@project_routes.delete("/delete/{project_id}")
def delete_project(project_id: int, session = Depends(get_session)):
    project = session.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    else:
        session.delete(project)
        session.commit()
        return {"message": f"Project with id {project_id} deleted successfully!"}
