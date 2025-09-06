from fastapi import FastAPI
from fastapi import APIRouter, HTTPException, status
from models.models import Student
from schemas.user_schemas import StudentIn, StudentOut, MessageOut

students = []

student_router = APIRouter(prefix="/students", tags=["Students"])

#Lista todos os estudantes
@student_router.get("/", response_model=list[StudentOut])
async def get_students() -> list[StudentOut]:
    if len(students) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No students found"
        )
    return students

#Cadastra um novo estudante
@student_router.post("/", response_model=MessageOut):
async def create_student(student_in: StudentIn) -> MessageOut:
    new_student = Student(**student_in.model_dump())
    students.append(new_student)
    return MessageOut(message="Student created successfully")

#Deleta um estudante específico pelo ID
@student_router.delete("/{student_id}", response_model=MessageOut)
async def delete_student(student_id: str) -> MessageOut:
    for student in students:
        if str(student.id) == student_id:
            students.remove(student)
            return MessageOut(message="Student deleted successfully")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )

#Lista informações de um estudante específico pelo ID
@student_router.get("/{student_id}", response_model=StudentOut)
async def get_student(student_id: str) -> StudentOut:
    for student in students:
        if str(student.id) == student_id:
            return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )

#Atualiza informações de um estudante específico pelo ID
@student_router.put("/{student_id}", response_model=MessageOut)

