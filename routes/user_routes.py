from fastapi import FastAPI, status, HTTPException, APIRouter
from schemas.user_schemas import UserIn, UserOut, MessageOut
from db import get_db
import sqlite3

user_router = APIRouter(prefix="/user", tags=["User Management"])


#Lista todos os usuarios 
@user_router.get("/", response_model=list[UserOut])
async def get_users() -> list[UserOut]:
    ''' Lista todos os usuários '''
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, tipo FROM Usuario")
    rows = cursor.fetchall()
    users = [UserOut(id=row[0], name=row[1], email=row[2], type=row[3], fl_active=True) for row in rows]
    conn.close()
    return users


#Cadastra um novo usuario
@user_router.post("/sign-up", response_model=MessageOut)
async def create_user(user_in: UserIn) -> MessageOut:
    ''' Cadastra um novo usuário '''

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Usuario (nome, email, senha, tipo) VALUES (?, ?, ?, ?)", 
                   (user_in.name, user_in.email, user_in.password, user_in.type))
    conn.commit()
    conn.close()
    return MessageOut(message="User created successfully")


'''
#Deleta um usuario específico pelo ID
@user_router.delete("/users/{user_id}", response_model=MessageOut)
async def delete_user(user_id: str) -> MessageOut:
    for user in users:
        if str(user.id) == user_id:
            users.remove(user)
            return MessageOut(message="User deleted successfully")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

#Lista informações de um usuario específico pelo ID
@user_router.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: str) -> UserOut:
    for user in users:
        if str(user.id) == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

#Atualiza informações de um usuario específico pelo ID
@user_router.put("/users/{user_id}", response_model=MessageOut)
async def update_user(user_id: str, user_in: UserIn) -> MessageOut:
    for index, user in enumerate(users):
        if str(user.id) == user_id:
            updated_user = user.copy(update=user_in.model_dump())
            users[index] = updated_user
            return MessageOut(message="User updated successfully")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

#Loga o usuário
@user_router.post("/login", response_model=MessageOut)
async def login(email: str, password: str) -> MessageOut:
    for user in users:
        if user.email == email and user.password == password:
            return MessageOut(message="Login successful")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password"
    )

'''