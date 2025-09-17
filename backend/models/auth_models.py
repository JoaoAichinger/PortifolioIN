from sqlalchemy import create_engine, Column, Integer, String, BOOLEAN, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

db = create_engine('sqlite:///database.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    type = Column("type", BOOLEAN, nullable=False)  # True for student, False for recruiter 

    def __init__(self, name: str, email: str, password: str, type: bool):
        self.name = name
        self.email = email
        self.password = password
        self.type = type

class Student(Base):
    __tablename__ = "student"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    course = Column("course", String, nullable=False)
    cell = Column("cell", String, nullable=False)

    def __init__(self, name, course, cell):
        self.name = name
        self.course = course
        self.cell = cell

# tabela associativa - serve para fazer o meio de campo entre Projetos e Tags.
project_tags = Table(  
    "project_tags",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("project.id")),
    Column("tag_id", Integer, ForeignKey("tags.id"))
)

class Project(Base):
    __tablename__ = "project"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    student_id = Column("student_id", Integer, ForeignKey("student.id"))
    title = Column("title", String, nullable=False)
    photo = Column("photo", String)
    description = Column("description", String)
    body = Column("corpo", String)


    def __init__(self, student_id, title, photo, description, body):
        self.student_id = student_id
        self.title = title
        self.photo = photo
        self.description = description
        self.body = body

    tags = relationship("Tags", secondary=project_tags, back_populates="project")

class Tags(Base):
    __tablename__ = "tags"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)

    def __init__(self, name):
        self.name = name   

    project = relationship("Project", secondary=project_tags, back_populates="tags")