from sqlalchemy import create_engine, Column, Integer, String, BOOLEAN
from sqlalchemy.orm import declarative_base 

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


