# Backend do Portfólio

Este diretório contém o código-fonte do backend do projeto de portfólio, desenvolvido com FastAPI e SQLAlchemy.

## Configuração e Execução

Para configurar e executar o backend localmente, siga os passos abaixo:

1.  **Navegue até o diretório do backend:**
    ```bash
    cd final_project/backend
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do diretório `backend` com o seguinte conteúdo:
    ```
    SECRET_KEY="sua_chave_secreta_aqui" # Use uma string longa e aleatória
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5.  **Popule o banco de dados (opcional, mas recomendado para testes):**
    Execute o script `populate_db_improved.py` para criar usuários de teste, estudantes, projetos e tags.
    ```bash
    python populate_db_improved.py
    ```
    Este script também exibirá as credenciais dos usuários de teste.

6.  **Inicie o servidor da API:**
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

O servidor da API estará disponível em `http://localhost:8000`. A documentação interativa (Swagger UI) estará em `http://localhost:8000/docs`.

## Estrutura do Projeto

O projeto segue uma estrutura modular para o backend:

```
backend/
├── alembic.ini             # Configuração do Alembic (migrações de banco de dados)
├── database.db             # Banco de dados SQLite (gerado)
├── dependencies.py         # Funções de dependência para FastAPI (e.g., sessão DB, verificação de token)
├── main.py                 # Ponto de entrada da aplicação FastAPI
├── migrations/             # Migrações de banco de dados (geradas pelo Alembic)
├── models/                 # Definições dos modelos SQLAlchemy (User, Student, Project, Tags)
├── populate_db.py          # Script original para popular o DB
├── populate_db_improved.py # Script melhorado para popular o DB com usuários de teste
├── pyproject.toml
├── requirements.txt        # Dependências do Python
├── routes/                 # Definições das rotas da API
│   ├── auth_routes.py      # Rotas de autenticação (login, sign-up)
│   ├── project_routes.py   # Rotas relacionadas a projetos
│   ├── students_routes.py  # Rotas relacionadas a estudantes
│   ├── tags_routes.py      # Rotas relacionadas a tags
│   └── profile_routes.py   # **NOVO:** Rotas para perfil do usuário
├── schemas/                # Schemas Pydantic para validação de dados
├── uv.lock
└── venv/                   # Ambiente virtual (se criado)
```

## Novas Funcionalidades e Alterações

### 1. Autenticação e Perfil do Usuário

-   **`populate_db_improved.py`:** Um novo script foi criado para popular o banco de dados com usuários de teste (estudantes e recrutadores) e senhas conhecidas (`123456`). Isso facilita os testes de login e o desenvolvimento.
-   **`routes/profile_routes.py`:** Nova rota adicionada para gerenciar o perfil do usuário logado (`/users/me`).
    -   `GET /users/me`: Retorna os dados do usuário logado.
    -   `PUT /users/me`: Permite atualizar o nome do usuário logado (pode ser expandido para outros campos).
-   **Integração com `main.py`:** A nova rota de perfil foi incluída no arquivo principal da aplicação.

### 2. Lógica de Filtragem de Estudantes

-   **`routes/students_routes.py`:** A lógica da rota `GET /students/list` foi modificada para atender ao requisito de 100% de compatibilidade na busca por tags.
    -   Agora, ao filtrar por múltiplas tags, apenas os estudantes que possuem **pelo menos um projeto que contenha TODAS as tags selecionadas** serão retornados.

## Testes

Após iniciar o backend, utilize as credenciais fornecidas pelo `populate_db_improved.py` para testar as funcionalidades de login, acesso ao perfil e a filtragem de estudantes por tags. Acesse `http://localhost:8000/docs` para interagir com a API via Swagger UI.

---
