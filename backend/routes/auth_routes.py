from fastapi import FastAPI, status, HTTPException, APIRouter, Depends
from schemas.auth_schemas import MessageOut, SignUpSchema, UserPublic, LoginSchema
from models.auth_models import User
from dependencies import get_session, verify_token
from sqlalchemy.orm import Session
from main import bcrypt_context, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm


auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

def create_token(user_id: str, duration: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    exp_date = datetime.now(tz=timezone.utc) + duration
    dict_info = {"exp": exp_date, "sub": str(user_id)}
    encoded_jwt = jwt.encode(dict_info, SECRET_KEY, ALGORITHM)  
    return encoded_jwt


def authenticate_user(email: str, password: str, session: Session):
    user = session.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False

    return user


#Cadastra um novo usuario
@auth_router.post("/sign-up", response_model=MessageOut)
def create_user(user_in: SignUpSchema, session: Session = Depends(get_session)):
    ''' Cadastra um novo usuário '''
    user = session.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        crypted_password = bcrypt_context.hash(user_in.password)
        new_user = User(name=user_in.name, email=user_in.email, password=crypted_password, type=user_in.type)
        session.add(new_user)
        session.commit()
        return MessageOut(message="User created successfully")

@auth_router.post("/login")
def login(user_in: LoginSchema, session: Session = Depends(get_session)):
    user = authenticate_user(user_in.email, user_in.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="Email not registered")
    else:
        access_token = create_token(user.id)
        refresh_token = create_token(user.id, duration=timedelta(days=7))
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@auth_router.post("/login-form")
def login_form(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="Email not registered")
    else:
        access_token = create_token(user.id)
        refresh_token = create_token(user.id, duration=timedelta(days=7))
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@auth_router.get("/refresh")
def refresh_token(user: User = Depends(verify_token)    ):
    ''' Gera um novo token de acesso '''
    access_token = create_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}



@auth_router.get("/users", response_model=list[UserPublic])
def get_users(session: Session = Depends(get_session), user: User = Depends(verify_token), name: str = None):
    ''' Retorna todos os usuários '''
    if not name:
        users = session.query(User).all()
    else:
        users = session.query(User).filter(User.name == name).all()
    return users

