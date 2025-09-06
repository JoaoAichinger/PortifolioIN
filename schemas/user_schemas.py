from pydantic import BaseModel, EmailStr
from uuid import UUID
from enum import Enum

class MessageOut(BaseModel):
    message: str

'''
class UserType(str, Enum):
    ADMIN = "admin"
    RECRUITER = "recruiter"
    STUDENT = "student"
'''

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    type: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    type: str


