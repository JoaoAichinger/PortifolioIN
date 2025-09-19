"""
Script melhorado para popular o banco de dados com dados reais de usuários, estudantes, projetos e tags.
Inclui usuários de teste para login com senhas conhecidas.
"""

from sqlalchemy.orm import sessionmaker
from models.auth_models import db, Base, User, Student, Project, Tags
from passlib.context import CryptContext
import random

# Configurar contexto de criptografia
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Criar as tabelas se não existirem
Base.metadata.create_all(db)

# Criar sessão
Session = sessionmaker(bind=db)
session = Session()

# Limpar dados existentes (opcional - descomente se quiser resetar)
print("Limpando dados existentes...")
session.query(Project).delete()
session.query(Student).delete()
session.query(Tags).delete()
session.query(User).delete()
session.commit()

# Dados de usuários de teste
print("Criando usuários de teste...")
test_users = [
    {
        "name": "Admin Teste",
        "email": "admin@teste.com",
        "password": "123456",
        "type": False  # Recrutador
    },
    {
        "name": "Ana Silva",
        "email": "ana@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Bruno Santos",
        "email": "bruno@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Carlos Oliveira",
        "email": "carlos@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Diana Costa",
        "email": "diana@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Eduardo Lima",
        "email": "eduardo@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Fernanda Rodrigues",
        "email": "fernanda@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Gabriel Pereira",
        "email": "gabriel@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Helena Martins",
        "email": "helena@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Igor Almeida",
        "email": "igor@teste.com",
        "password": "123456",
        "type": True  # Estudante
    },
    {
        "name": "Recrutador Tech",
        "email": "recrutador@teste.com",
        "password": "123456",
        "type": False  # Recrutador
    }
]

# Criar usuários
users_objects = []
for user_data in test_users:
    crypted_password = bcrypt_context.hash(user_data["password"])
    user = User(
        name=user_data["name"],
        email=user_data["email"],
        password=crypted_password,
        type=user_data["type"]
    )
    session.add(user)
    users_objects.append(user)

session.commit()

# Dados de tags
tags_data = [
    "Python", "JavaScript", "React", "Node.js", "Django", "Flask", 
    "HTML", "CSS", "TypeScript", "Vue.js", "Angular", "Express",
    "MongoDB", "PostgreSQL", "MySQL", "SQLite", "Redis", "Docker",
    "AWS", "Azure", "Git", "GitHub", "Linux", "Machine Learning",
    "Data Science", "AI", "Mobile", "Android", "iOS", "Flutter",
    "React Native", "UI/UX", "Design", "Figma", "Photoshop", "Illustrator",
    "Java", "C++", "C#", ".NET", "Spring", "Bootstrap", "Sass", "Less",
    "Webpack", "Vite", "Next.js", "Nuxt.js", "GraphQL", "REST API",
    "Microservices", "Kubernetes", "Jenkins", "CI/CD", "Testing", "Jest"
]

# Criar tags
print("Criando tags...")
tags_objects = []
for tag_name in tags_data:
    tag = Tags(tag_name)
    session.add(tag)
    tags_objects.append(tag)

session.commit()

# Dados de estudantes (correspondentes aos usuários estudantes)
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
    student = Student(student_data["name"], student_data["course"], student_data["cell"])
    session.add(student)
    students_objects.append(student)

session.commit()

# Dados de projetos variados
projects_data = [
    {
        "title": "Sistema de Gestão Escolar",
        "photo": "https://www.totvs.com/educacao/",
        "description": "Sistema completo para gestão de escolas com controle de alunos, professores e notas.",
        "body": "Um sistema web desenvolvido em Python com Django para gerenciar todas as atividades de uma escola. Inclui módulos para cadastro de alunos, professores, disciplinas, notas e relatórios. Interface responsiva e intuitiva com dashboard administrativo completo.",
        "tags": ["Python", "Django", "PostgreSQL", "HTML", "CSS", "JavaScript", "Bootstrap"]
    },
    {
        "title": "E-commerce Moderno",
        "photo": "https://www.americanas.com.br/",
        "description": "Plataforma de e-commerce com carrinho de compras, pagamento online e painel administrativo.",
        "body": "E-commerce desenvolvido com React no frontend e Node.js no backend. Integração com APIs de pagamento, sistema de autenticação JWT, carrinho de compras persistente e painel administrativo completo. Implementa microservices e containerização com Docker.",
        "tags": ["React", "Node.js", "Express", "MongoDB", "JavaScript", "HTML", "CSS", "Docker", "Microservices"]
    },
    {
        "title": "App de Delivery Mobile",
        "photo": "https://www.ifood.com.br/",
        "description": "Aplicativo mobile para delivery de comida com geolocalização e pagamento integrado.",
        "body": "Aplicativo desenvolvido em React Native com funcionalidades de geolocalização, integração com APIs de pagamento, sistema de avaliações e chat em tempo real entre cliente e entregador. Utiliza Firebase para notificações push.",
        "tags": ["React Native", "Mobile", "JavaScript", "Node.js", "MongoDB", "Firebase", "Android", "iOS"]
    },
    {
        "title": "Dashboard Analytics com IA",
        "photo": "https://www.tableau.com/",
        "description": "Dashboard interativo para análise de dados com gráficos e relatórios em tempo real usando IA.",
        "body": "Dashboard desenvolvido com Vue.js e D3.js para visualização de dados. Conecta-se a múltiplas fontes de dados, gera relatórios automáticos com Machine Learning e permite análises preditivas com filtros avançados.",
        "tags": ["Vue.js", "JavaScript", "Data Science", "Python", "PostgreSQL", "HTML", "CSS", "AI", "Machine Learning"]
    },
    {
        "title": "Sistema de Blog com CMS",
        "photo": "https://wordpress.com/",
        "description": "Plataforma de blog com editor de texto rico e sistema de comentários avançado.",
        "body": "Sistema de blog desenvolvido com Flask e PostgreSQL. Inclui editor WYSIWYG, sistema de comentários com moderação, categorias, tags, busca avançada, SEO otimizado e painel administrativo para gerenciamento de conteúdo.",
        "tags": ["Python", "Flask", "PostgreSQL", "HTML", "CSS", "JavaScript", "SEO", "CMS"]
    },
    {
        "title": "Portfolio Interativo 3D",
        "photo": "https://tympanus.net/Development/CreativePortfolio/",
        "description": "Site portfolio responsivo com animações 3D e design moderno.",
        "body": "Portfolio pessoal desenvolvido com HTML5, CSS3, JavaScript e Three.js. Design responsivo, animações 3D interativas, integração com APIs do GitHub, formulário de contato funcional e otimização para performance.",
        "tags": ["HTML", "CSS", "JavaScript", "Design", "UI/UX", "Figma", "Three.js", "WebGL"]
    },
    {
        "title": "API RESTful Microservices",
        "photo": "https://swagger.io/",
        "description": "API RESTful escalável com arquitetura de microservices e autenticação JWT.",
        "body": "API desenvolvida em Node.js com Express, implementando padrões REST e arquitetura de microservices. Inclui autenticação JWT, validação de dados, documentação Swagger, testes automatizados com Jest e deploy com Kubernetes.",
        "tags": ["Node.js", "Express", "JavaScript", "MongoDB", "JWT", "Docker", "Kubernetes", "Microservices", "Testing"]
    },
    {
        "title": "Jogo Web 2D Multiplayer",
        "photo": "https://www.miniclip.com/games/en/",
        "description": "Jogo 2D multiplayer desenvolvido em JavaScript com Canvas API e WebSockets.",
        "body": "Jogo de plataforma 2D multiplayer desenvolvido com JavaScript puro, Canvas API e Socket.io. Implementa sistema de física avançado, detecção de colisões, sistema de pontuação global, salas de jogo e chat em tempo real.",
        "tags": ["JavaScript", "HTML", "CSS", "Canvas", "WebSockets", "Socket.io", "Game Development", "Multiplayer"]
    },
    {
        "title": "Chatbot IA com NLP",
        "photo": "https://chat.openai.com/",
        "description": "Chatbot inteligente com processamento de linguagem natural e aprendizado de máquina.",
        "body": "Chatbot desenvolvido em Python com processamento de linguagem natural usando NLTK e spaCy. Integração com APIs externas, sistema de aprendizado contínuo, análise de sentimentos e interface web responsiva com React.",
        "tags": ["Python", "AI", "Machine Learning", "NLTK", "Flask", "JavaScript", "React", "NLP", "Data Science"]
    }
]


# Criar múltiplos projetos para cada estudante para ter mais variedade
print("Criando projetos...")
project_combinations = [
    # Ana Silva - Foco em Python e Web
    [0, 4, 8],  # Sistema Escolar, Blog, Chatbot IA
    # Bruno Santos - Foco em JavaScript e Mobile
    [1, 2, 6],  # E-commerce, App Delivery, Portfolio 3D
    # Carlos Oliveira - Foco em Full Stack
    [6, 7, 3],  # API RESTful, Jogo Web, Dashboard Analytics
    # Diana Costa - Foco em Design e Frontend
    [5, 1, 7],  # Portfolio 3D, E-commerce, Jogo Web
    # Eduardo Lima - Foco em Backend e APIs
    [6, 0, 8],  # API RESTful, Sistema Escolar, Chatbot IA
    # Fernanda Rodrigues - Foco em Data Science
    [3, 8, 4],  # Dashboard Analytics, Chatbot IA, Blog
    # Gabriel Pereira - Foco em Mobile e Games
    [2, 7, 1],  # App Delivery, Jogo Web, E-commerce
    # Helena Martins - Foco em Design e UX
    [5, 1, 3],  # Portfolio 3D, E-commerce, Dashboard Analytics
    # Igor Almeida - Foco em DevOps e Infraestrutura
    [6, 1, 0]   # API RESTful, E-commerce, Sistema Escolar
]

for i, student in enumerate(students_objects):
    project_indices = project_combinations[i]
    
    for project_index in project_indices:
        project_data = projects_data[project_index]
        
        # Criar título único para cada projeto
        unique_title = f"{project_data['title']} - {student.name}"
        
        project = Project(
            student.id,
            unique_title,
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

print("\n" + "="*60)
print("BANCO DE DADOS POPULADO COM SUCESSO!")
print("="*60)
print(f"✅ Total de usuários criados: {len(users_objects)}")
print(f"✅ Total de estudantes criados: {len(students_objects)}")
print(f"✅ Total de tags criadas: {len(tags_objects)}")
print(f"✅ Total de projetos criados: {session.query(Project).count()}")

print("\n" + "="*60)
print("USUÁRIOS DE TESTE PARA LOGIN:")
print("="*60)
print("📧 Email: admin@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Recrutador")
print("📧 Email: ana@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: bruno@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: carlos@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: diana@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: eduardo@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: fernanda@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: gabriel@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: helena@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: igor@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Estudante")
print("📧 Email: recrutador@teste.com | 🔑 Senha: 123456 | 👤 Tipo: Recrutador")

print("\n" + "="*60)
print("FUNCIONALIDADES IMPLEMENTADAS:")
print("="*60)
print("🔐 Sistema de autenticação com JWT")
print("👥 Usuários de teste com senhas conhecidas")
print("🏷️ Sistema de tags para filtros avançados")
print("🔍 Busca por tags com compatibilidade 100%")
print("📱 Interface responsiva e moderna")
print("🎨 Design melhorado para login e perfil")
print("📊 Múltiplos projetos por estudante")
print("🏢 Diferenciação entre estudantes e recrutadores")

print("\n" + "="*60)
print("PRÓXIMOS PASSOS:")
print("="*60)
print("1. Execute o backend: python main.py")
print("2. Execute o frontend: npm run dev")
print("3. Teste o login com os usuários acima")
print("4. Teste a busca por tags")
print("5. Teste o carrossel de projetos")
print("="*60)

session.close()
