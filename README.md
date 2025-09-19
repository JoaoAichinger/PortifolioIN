# Portfólio Hackathon City - Versão Aprimorada

<p align="center">
  <img src="./frontend/src/assets/backgroundimg1.png" height="300" alt="Banner do Projeto"/>
</p>

<h1 align="center">Portfólio Hackathon City 🚀</h1>

<p align="center">
  <b>Bem-vindo à versão aprimorada do projeto de portfólio da Infinity School!</b><br>
  Esta versão inclui novas funcionalidades de login, um perfil de usuário completo e melhorias significativas no backend e frontend.
</p>

---

## Sobre o Projeto

Este repositório contém o projeto de portfólio aprimorado, com o objetivo de fornecer uma plataforma robusta e profissional para que os alunos da Infinity School possam exibir seus projetos, habilidades e se conectar com recrutadores.

## Estrutura do Projeto

O projeto está organizado em dois diretórios principais, mantendo uma separação clara entre o frontend e o backend:

-   **`frontend/`**: Contém a aplicação React (Vite) responsável por toda a interface do usuário e interação com o cliente.
-   **`backend/`**: Contém a API desenvolvida com FastAPI, que gerencia os dados, a lógica de negócios e a autenticação.

Além disso, cada diretório possui seu próprio `README.md` com instruções detalhadas sobre configuração, execução e funcionalidades específicas.

## Como Executar o Projeto Completo

Para executar o projeto, você precisará iniciar o servidor do backend e o servidor de desenvolvimento do frontend em terminais separados.

### 1. Executar o Backend

Primeiro, navegue até o diretório `backend` e siga as instruções detalhadas em seu `README.md`.

```bash
# Navegue até o diretório do backend
cd backend

# (Opcional, mas recomendado) Crie e ative um ambiente virtual
python3.11 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Popule o banco de dados com dados de teste
python populate_db_improved.py

# Inicie o servidor
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Executar o Frontend

Em um novo terminal, navegue até o diretório `frontend` e siga as instruções de seu `README.md`.

```bash
# Navegue até o diretório do frontend
cd frontend

# Instale as dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

Após iniciar ambos os servidores, a aplicação estará disponível em **`http://localhost:5173`** (ou a porta que o Vite indicar).

## Principais Funcionalidades Implementadas

-   **Sistema de Autenticação Moderno:**
    -   Interface de login em formato de modal, com design aprimorado.
    -   Autenticação segura utilizando JWT (JSON Web Tokens).

-   **Página de Perfil Completa:**
    -   Página de perfil de usuário com design profissional.
    -   Exibição de informações detalhadas: nome, bio, habilidades e projetos.
    -   Funcionalidade de edição de perfil, incluindo a troca da imagem.

-   **Busca Avançada por Tags:**
    -   A lógica de filtragem foi aprimorada para garantir **100% de compatibilidade**.
    -   Ao selecionar múltiplas tags, o sistema retorna apenas estudantes que possuem projetos com **todas** as tags selecionadas.

-   **Melhorias na Usabilidade:**
    -   A logo no cabeçalho agora redireciona para a página inicial.
    -   O carrossel de projetos foi ajustado para exibir grupos de 3, com suporte para grupos menores no final da lista.

-   **Backend Robusto e Organizado:**
    -   Adição de rotas específicas para o perfil do usuário.
    -   Criação de um script (`populate_db_improved.py`) para popular o banco de dados com dados de teste consistentes, incluindo usuários com senhas conhecidas para facilitar a demonstração e os testes.

## Testes Recomendados

Para garantir a qualidade e o funcionamento de todas as funcionalidades, sugerimos uma maratona de testes, cobrindo os seguintes cenários:

1.  **Login e Logout:** Teste o login com diferentes tipos de usuário (estudante e recrutador) e verifique se o logout funciona corretamente.
2.  **Edição de Perfil:** Acesse a página de perfil, edite as informações e a imagem, e confirme se as alterações são salvas.
3.  **Busca por Tags:**
    -   Selecione uma única tag e verifique os resultados.
    -   Selecione múltiplas tags e confirme que apenas estudantes com 100% de compatibilidade são exibidos.
    -   Combine a busca por tags com a busca por termos (nome do estudante/projeto).
4.  **Navegação:** Verifique se todos os links e botões de navegação (como a logo e o botão de perfil) estão funcionando como esperado.

---

<p align="center">
  <b>Infinity School • Construindo o futuro, hoje.</b>
</p>

