from pydantic import BaseModel, EmailStr
from typing import Optional, List

class MessageOut(BaseModel):
    message: str


class SignUpSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    type: bool  # True for student, False for recruiter
    cell: Optional[str] = None
    course: Optional[str] = None
    company: Optional[str] = None

    class Config:
        from_attributes = True    


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    type: bool  # True for student, False for recruiter
    fl_active: Optional[bool] = True

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class StudentSchemas(BaseModel):
    name: str
    course: str
    cell: str

    class Config:
        from_attributes = True

class TagSchemas(BaseModel):
    name: str

    class Config:
        from_attributes = True

class ProjectSchemasCadastrar(BaseModel):
    title: str
    photo: str
    description: str
    body: str
    tags: list[int] = []
    
    class Config:
        model_config = {
        "from_attributes": True  
    }
        
# Schema used to list projects - (output)
class ProjectSchemas(BaseModel):
    #student_id: int
    title: str
    photo: str
    description: str
    body: str
    tags: List[int]

    class Config:
        from_attributes = True