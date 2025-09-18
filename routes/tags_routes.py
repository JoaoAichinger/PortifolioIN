from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import delete
from typing import List
from models.auth_models import Tags, Project
from dependencies import get_session
from schemas.auth_schemas import ProjectSchemas, TagSchemas
from sqlalchemy.orm import joinedload  #joinedload carrega todas as tags de cada projeto

tags_routes = APIRouter(prefix="/tag", tags=["Tags"])

@tags_routes.post("/register")
async def register_tag(tag_schema: TagSchemas, session = Depends(get_session)):
    tag = session.query(Tags).filter(Tags.name==tag_schema.name).first()
    if tag:
        raise(HTTPException(status_code=400, detail="Tag already registered."))
    else:
        new_tag = Tags(tag_schema.name)
        session.add(new_tag)
        session.commit()
        return{"message": f"tag successfully registered - {tag_schema.name}"}
    

@tags_routes.get("/list")
def list_tags(session = Depends(get_session)):
    all_tags = session.query(Tags).all()
    if not all_tags:
       raise HTTPException(status_code=404, detail="There are no registered tags.")
    else: 
        return [{"id": tag.id, "name": tag.name} for tag in all_tags]

@tags_routes.get("/tags/search_projects", response_model=List[ProjectSchemas])
def search_projects_by_tag(tags_id:List[int]=Query(...), session= Depends(get_session)):
    projects = (session.query(Project).options(joinedload(Project.tags)).join(Project.tags).filter(Tags.id.in_(tags_id)).all())
    if not projects:
        raise HTTPException(status_code=404, detail="No projects found with these tags")
    result = []
    for project in projects:
        proj_dict = {
            "id": project.id,
            "student_id": project.student_id,
            "title": project.title,
            "photo": project.photo,
            "description": project.description,
            "body": project.body,
            "tags": [tag.id for tag in project.tags] 
        }
        result.append(proj_dict)
    
    return result
        
@tags_routes.put("/edit/{tag_id}")
def edit_tag(tag_id: int, tag_schema: TagSchemas, session = Depends(get_session)):
    tag = session.query(Tags).filter(Tags.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found.")
    else:
        tag.name = tag_schema.name
        session.commit()
        return {"message": f"Tag with id {tag_id} updated successfully"}
    
@tags_routes.delete("/delete/{tags_id}")
def delete_tag(tag_id: int, session = Depends(get_session)):
    tag = session.query(Tags).filter(Tags.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found.")
    else:
        session.delete(tag)
        session.commit()
        return {"message": f"Tag with id {tag_id} deleted successfully!"}
    


