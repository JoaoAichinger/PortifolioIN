from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete
from models.auth_models import Project, Tags, Student, User
from dependencies import get_session, verify_token
from schemas.auth_schemas import ProjectSchemas, ProjectSchemasCadastrar
from sqlalchemy.orm import Session

project_routes = APIRouter(prefix="/project", tags=["Projects"])


@project_routes.post("/register")
async def register_project(project_schema: ProjectSchemasCadastrar, session: Session = Depends(get_session), user: User = Depends(verify_token)):
    student = session.query(Student).filter(Student.user_id == user.id).first()
    if not student:
        raise HTTPException(status_code=400, detail="Student not found")
    new_project = Project(
        student_id=student.id,
        title=project_schema.title,
        photo=project_schema.photo,
        description=project_schema.description,
        body=project_schema.body
    )
    session.add(new_project)

    for tag_id in project_schema.tags:
        tag = session.query(Tags).filter(Tags.id == tag_id).first()
        if tag:
            new_project.tags.append(tag)

    session.commit()
    session.refresh(new_project)

    return {"message": f"Project '{project_schema.title}' successfully registered!"}

@project_routes.get("/list")
def list_projects(session = Depends(get_session), user: User = Depends(verify_token)):
    student = session.query(Student).filter(Student.user_id == user.id).first()
    if not student:
        raise HTTPException(status_code=404, detail="There are no registered projects.")
    else:
        projects = session.query(Project).filter(Project.student_id == student.id).all()
        if not projects:
            raise HTTPException(status_code=404, detail="There are no registered projects.")
        return [{"id": project.id, "title": project.title, "photo": project.photo ,"descrição": project.description, "body": project.body} for project in projects]
        

@project_routes.get("/list_all_projects")
def list_projects_student(session = Depends(get_session)):
    all_project = session.query(Project).all()
    if not all_project:
        raise HTTPException(status_code=404, detail="There are no registered projects.")
    else:
        return [{"id": project.id, "title": project.title, "photo": project.photo ,"descrição": project.description, "body": project.body} for project in all_project]
        
@project_routes.put("/edit")
def edit_project(project_id: int, project_schema: ProjectSchemas, session = Depends(get_session), user: User = Depends(verify_token)):
    student = session.query(Student).filter(Student.user_id == user.id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    project = session.query(Project).filter(Project.id == project_id, Project.student_id == student.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found or you do not have permission to edit it.")

    else:
        project.title = project_schema.title
        project.photo = project_schema.photo
        project.description = project_schema.description
        project.body = project_schema.body
        project.tags.clear()
        for tag_id in project_schema.tags:
            tag = session.query(Tags).filter(Tags.id == tag_id).first()
            if tag:
                project.tags.append(tag)

        session.commit()
        session.refresh(project)
        return {"message": f"Project with title {project_schema.title} successfully edited!"}
    
@project_routes.delete("/delete")
def delete_project(project_id: int, session = Depends(get_session), user: User = Depends(verify_token)):
    project = session.query(Project).filter(Project.id == project_id, Project.student.has(user_id=user.id)).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    else:
        session.delete(project)
        session.commit()
        return {"message": f"Project with id {project_id} deleted successfully!"}

