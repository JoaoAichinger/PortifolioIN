from models.auth_models import db
from sqlalchemy.orm import sessionmaker, Session
from models.auth_models import User
from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
import os

# Importar as configurações diretamente
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login-form")

def get_session():
    try:
        SessionLocal = sessionmaker(bind=db)
        session = SessionLocal()
        yield session
    finally:
        session.close()


def verify_token(token: str = Depends(oauth2_schema), session: Session = Depends(get_session)):
    try:
        dict_info = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_user = dict_info.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = session.query(User).filter(User.id == id_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
