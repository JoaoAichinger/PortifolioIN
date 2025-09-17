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

class Aluno(Base):
    __tablename__ = "aluno"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    curso = Column("curso", String)
    celular = Column("celular", String)

    def __init__(self, nome, celular, curso):
        self.nome = nome
        self.curso = curso
        self.celular = celular

# tabela associativa - serve para fazer o meio de campo entre Projetos e Tags.
projeto_Tags = Table(  
    "projeto_tags",
    Base.metadata,
    Column("projeto_id", Integer, ForeignKey("projetos.id")),
    Column("tag_id", Integer, ForeignKey("tags.id"))
)

class Projetos(Base):
    __tablename__ = "projetos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    aluno_id = Column("aluno_id", Integer, ForeignKey("aluno.id"))
    titulo = Column("titulo", String)
    foto = Column("foto", String)
    descricao = Column("descricao", String)
    corpo = Column("corpo", String)

    def __init__(self, aluno_id ,titulo, foto, descricao, corpo):
        self.aluno_id = aluno_id
        self.titulo = titulo
        self.foto = foto
        self.descricao = descricao
        self.corpo = corpo

    tags = relationship("Tags", secondary=projeto_Tags, back_populates="projetos")

class Tags(Base):
    __tablename__ = "tags"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)

    def __init__(self, nome):
        self.nome = nome   

    projetos = relationship("Projetos", secondary=projeto_Tags, back_populates="tags")