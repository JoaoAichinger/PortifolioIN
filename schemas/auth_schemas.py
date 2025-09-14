from pydantic import BaseModel, EmailStr
from typing import Optional

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


