from pydantic import BaseModel, EmailStr
from typing import Optional, List

class MessageOut(BaseModel):
    message: str


class SignUpSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    type: bool  # True for student, False for recruiter

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


class AlunoSchemas(BaseModel):
    nome: str
    curso: str
    celular: str

    class Config:
        from_attributes = True

class TagsSchemas(BaseModel):
    nome: str

    class Config:
        from_attributes = True

class ProjetosSchemasCadastrar(BaseModel):
    aluno_id: int
    titulo: str
    foto: str
    descricao: str
    corpo: str
    tags: list[int] = []
    
    class Config:
        model_config = {
        "from_attributes": True  
    }
        
# Schema usado para listar projetos - (saída)
class ProjetosSchemas(BaseModel):
    aluno_id: int
    titulo: str
    foto: str
    descricao: str
    corpo: str
    tags: List[TagsSchemas] = []

    class Config:
        from_attributes = True