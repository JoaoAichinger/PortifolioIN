from fastapi import APIRouter, Depends, HTTPException
from schemas.auth_schemas import UserPublic
from models.auth_models import User
from dependencies import verify_token
from sqlalchemy.orm import Session
from dependencies import get_session

profile_router = APIRouter(prefix="/users", tags=["Profile"])

@profile_router.get("/me", response_model=UserPublic)
def get_current_user_profile(user: User = Depends(verify_token)):
    """Retorna o perfil do usuário logado"""
    return user

@profile_router.put("/me")
def update_current_user_profile(
    name: str = None,
    user: User = Depends(verify_token),
    session: Session = Depends(get_session)
):
    """Atualiza o perfil do usuário logado"""
    if name:
        user.name = name
        session.commit()
        session.refresh(user)
    
    return {"message": "Profile updated successfully", "user": user}
