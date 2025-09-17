from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete
from models.auth_models import Student
from dependencies import get_session
from schemas.auth_schemas import StudentSchemas
from sqlalchemy.orm import Session


students_routes =  APIRouter(prefix="/students", tags=["Students"])

@students_routes.post("/register")
async def register_student(student_schemas: StudentSchemas, session = Depends(get_session)):
    student = session.query(Student).filter(Student.name==student_schemas.name).first()
    if student:
        raise HTTPException(status_code=400, detail="Student já cadastrado.")
    else:
        new_student = Student(student_schemas.name, student_schemas.cell, student_schemas.course)
        session.add(new_student)
        session.commit()
        return{"message": f"student {student_schemas.name} successfully registered!"}
    
@students_routes.get("/list")
def list_students(session = Depends(get_session)):
    all_students = session.query(Student).all()
    if not all_students:
        raise HTTPException(status_code=404, detail="There are no registered students.")
    else:
        return [{"name": student.name, "course": student.course, "phone": student.cell} for student in all_students]
    
@students_routes.put("/edit/{student_id}")
def edit_students(student_id: int, student_schemas: StudentSchemas, session=Depends(get_session)):
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="We did not find this student in the system.")
    else:
        student.name = student_schemas.name
        student.course = student_schemas.course
        student.cell = student_schemas.cell
        session.commit()
        return{"message": f"Student {student.name} updated successfully!"}
