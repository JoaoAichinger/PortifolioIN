# Infinity API - Backend

## Descrição
API desenvolvida em FastAPI para gerenciar usuários, estudantes, projetos e tags.

## Estrutura
- **Backend:** FastAPI + SQLAlchemy + SQLite
- **Frontend:** React (Vite) - integração planejada

## Instalação
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints Principais
- **Auth**
  - POST /auth/sign-up
  - POST /auth/login
  - GET /auth/refresh
  - GET /auth/users

- **Students**
  - POST /students/register
  - GET /students/list
  - PUT /students/edit/{student_id}

- **Projects**
  - POST /project/register
  - GET /project/list
  - PUT /project/edit/{project_id}
  - DELETE /project/delete/{project_id}

- **Tags**
  - POST /tag/register
  - GET /tag/list
  - GET /tag/tags/search_projects?tags_id=1&tags_id=2
  - PUT /tag/edit/{tag_id}
  - DELETE /tag/delete/{tag_id}

## Banco de Dados
- users (id, name, email, password, type)
- student (id, name, course, cell)
- project (id, student_id, title, photo, description, corpo)
- tags (id, name)
- project_tags (project_id, tag_id)

## Problemas Conhecidos
- Inconsistência: coluna `corpo` vs `body`
- Decorator/param desincronizado em rotas
- Trechos de código inacabados com `...`
- Fluxo de refresh token simplificado demais

## Integração Frontend
- Criar serviços em `src/services/api.js` com `fetch`
- Criar `AuthContext` em `src/contexts/AuthContext.jsx`
- Implementar `LoginForm.jsx`

## Testes
Abrir `http://localhost:8000/docs` para testar via Swagger UI.
