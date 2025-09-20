"""
Script para popular o banco de dados com dados reais de estudantes, projetos e tags.
"""

from sqlalchemy.orm import sessionmaker
from models.auth_models import db, Base, Student, Project, Tags
import random

# Criar as tabelas se não existirem
Base.metadata.create_all(db)

# Criar sessão
Session = sessionmaker(bind=db)
session = Session()

# Limpar dados existentes (opcional - descomente se quiser resetar)
# session.query(Project).delete()
# session.query(Student).delete()
# session.query(Tags).delete()
# session.commit()

# Dados de tags
tags_data = [
    "Python", "JavaScript", "React", "Node.js", "Django", "Flask", 
    "HTML", "CSS", "TypeScript", "Vue.js", "Angular", "Express",
    "MongoDB", "PostgreSQL", "MySQL", "SQLite", "Redis", "Docker",
    "AWS", "Azure", "Git", "GitHub", "Linux", "Machine Learning",
    "Data Science", "AI", "Mobile", "Android", "iOS", "Flutter",
    "React Native", "UI/UX", "Design", "Figma", "Photoshop", "Illustrator"
]

# Criar tags
print("Criando tags...")
tags_objects = []
for tag_name in tags_data:
    existing_tag = session.query(Tags).filter(Tags.name == tag_name).first()
    if not existing_tag:
        tag = Tags(tag_name)
        session.add(tag)
        tags_objects.append(tag)
    else:
        tags_objects.append(existing_tag)

session.commit()

# Dados de estudantes
students_data = [
    {
        "name": "Ana Silva",
        "course": "Ciência da Computação",
        "cell": "(11) 99999-1111"
    },
    {
        "name": "Bruno Santos",
        "course": "Engenharia de Software",
        "cell": "(11) 99999-2222"
    },
    {
        "name": "Carlos Oliveira",
        "course": "Sistemas de Informação",
        "cell": "(11) 99999-3333"
    },
    {
        "name": "Diana Costa",
        "course": "Design Digital",
        "cell": "(11) 99999-4444"
    },
    {
        "name": "Eduardo Lima",
        "course": "Análise e Desenvolvimento de Sistemas",
        "cell": "(11) 99999-5555"
    },
    {
        "name": "Fernanda Rodrigues",
        "course": "Ciência da Computação",
        "cell": "(11) 99999-6666"
    },
    {
        "name": "Gabriel Pereira",
        "course": "Engenharia de Software",
        "cell": "(11) 99999-7777"
    },
    {
        "name": "Helena Martins",
        "course": "Design Digital",
        "cell": "(11) 99999-8888"
    },
    {
        "name": "Igor Almeida",
        "course": "Sistemas de Informação",
        "cell": "(11) 99999-9999"
    }
]

# Criar estudantes
print("Criando estudantes...")
students_objects = []
for student_data in students_data:
    existing_student = session.query(Student).filter(Student.name == student_data["name"]).first()
    if not existing_student:
        student = Student(student_data["name"], student_data["course"], student_data["cell"])
        session.add(student)
        students_objects.append(student)
    else:
        students_objects.append(existing_student)

session.commit()

# Dados de projetos
projects_data = [
    {
        "title": "Sistema de Gestão Escolar",
        "photo": "https://via.placeholder.com/400x300/4CAF50/white?text=Sistema+Escolar",
        "description": "Sistema completo para gestão de escolas com controle de alunos, professores e notas.",
        "body": "Um sistema web desenvolvido em Python com Django para gerenciar todas as atividades de uma escola. Inclui módulos para cadastro de alunos, professores, disciplinas, notas e relatórios. Interface responsiva e intuitiva.",
        "tags": ["Python", "Django", "PostgreSQL", "HTML", "CSS", "JavaScript"]
    },
    {
        "title": "E-commerce Moderno",
        "photo": "https://via.placeholder.com/400x300/2196F3/white?text=E-commerce",
        "description": "Plataforma de e-commerce com carrinho de compras, pagamento online e painel administrativo.",
        "body": "E-commerce desenvolvido com React no frontend e Node.js no backend. Integração com APIs de pagamento, sistema de autenticação JWT, carrinho de compras persistente e painel administrativo completo.",
        "tags": ["React", "Node.js", "Express", "MongoDB", "JavaScript", "HTML", "CSS"]
    },
    {
        "title": "App de Delivery",
        "photo": "https://via.placeholder.com/400x300/FF9800/white?text=Delivery+App",
        "description": "Aplicativo mobile para delivery de comida com geolocalização e pagamento integrado.",
        "body": "Aplicativo desenvolvido em React Native com funcionalidades de geolocalização, integração com APIs de pagamento, sistema de avaliações e chat em tempo real entre cliente e entregador.",
        "tags": ["React Native", "Mobile", "JavaScript", "Node.js", "MongoDB", "Firebase"]
    },
    {
        "title": "Dashboard Analytics",
        "photo": "https://via.placeholder.com/400x300/9C27B0/white?text=Analytics+Dashboard",
        "description": "Dashboard interativo para análise de dados com gráficos e relatórios em tempo real.",
        "body": "Dashboard desenvolvido com Vue.js e D3.js para visualização de dados. Conecta-se a múltiplas fontes de dados, gera relatórios automáticos e permite análises interativas com filtros avançados.",
        "tags": ["Vue.js", "JavaScript", "Data Science", "Python", "PostgreSQL", "HTML", "CSS"]
    },
    {
        "title": "Sistema de Blog",
        "photo": "https://via.placeholder.com/400x300/607D8B/white?text=Blog+System",
        "description": "Plataforma de blog com editor de texto rico e sistema de comentários.",
        "body": "Sistema de blog desenvolvido com Flask e SQLite. Inclui editor WYSIWYG, sistema de comentários, categorias, tags, busca avançada e painel administrativo para gerenciamento de conteúdo.",
        "tags": ["Python", "Flask", "SQLite", "HTML", "CSS", "JavaScript"]
    },
    {
        "title": "Portfolio Interativo",
        "photo": "https://via.placeholder.com/400x300/795548/white?text=Portfolio",
        "description": "Site portfolio responsivo com animações e design moderno.",
        "body": "Portfolio pessoal desenvolvido com HTML5, CSS3 e JavaScript vanilla. Design responsivo, animações CSS, integração com APIs do GitHub e formulário de contato funcional.",
        "tags": ["HTML", "CSS", "JavaScript", "Design", "UI/UX", "Figma"]
    },
    {
        "title": "API RESTful",
        "photo": "https://via.placeholder.com/400x300/3F51B5/white?text=REST+API",
        "description": "API RESTful para gerenciamento de tarefas com autenticação JWT.",
        "body": "API desenvolvida em Node.js com Express, implementando padrões REST. Inclui autenticação JWT, validação de dados, documentação Swagger e testes automatizados com Jest.",
        "tags": ["Node.js", "Express", "JavaScript", "MongoDB", "JWT", "Docker"]
    },
    {
        "title": "Jogo Web 2D",
        "photo": "https://via.placeholder.com/400x300/E91E63/white?text=Web+Game",
        "description": "Jogo 2D desenvolvido em JavaScript com Canvas API e física simples.",
        "body": "Jogo de plataforma 2D desenvolvido com JavaScript puro e Canvas API. Implementa sistema de física simples, detecção de colisões, sistema de pontuação e níveis progressivos.",
        "tags": ["JavaScript", "HTML", "CSS", "Canvas", "Game Development"]
    },
    {
        "title": "Chatbot Inteligente",
        "photo": "https://via.placeholder.com/400x300/009688/white?text=AI+Chatbot",
        "description": "Chatbot com processamento de linguagem natural e integração com APIs.",
        "body": "Chatbot desenvolvido em Python com processamento de linguagem natural usando NLTK. Integração com APIs externas, sistema de aprendizado e interface web responsiva.",
        "tags": ["Python", "AI", "Machine Learning", "NLTK", "Flask", "JavaScript"]
    }
]

# Criar projetos para cada estudante
print("Criando projetos...")
for i, student in enumerate(students_objects):
    project_data = projects_data[i]
    
    # Verificar se o projeto já existe
    existing_project = session.query(Project).filter(
        Project.student_id == student.id,
        Project.title == project_data["title"]
    ).first()
    
    if not existing_project:
        project = Project(
            student.id,
            project_data["title"],
            project_data["photo"],
            project_data["description"],
            project_data["body"]
        )
        
        # Adicionar tags ao projeto
        for tag_name in project_data["tags"]:
            tag = session.query(Tags).filter(Tags.name == tag_name).first()
            if tag:
                project.tags.append(tag)
        
        session.add(project)

session.commit()

print("Banco de dados populado com sucesso!")
print(f"Total de estudantes: {len(students_objects)}")
print(f"Total de tags: {len(tags_objects)}")
print("Cada estudante tem um projeto associado.")

session.close()

