# Frontend do Portfólio

Este diretório contém o código-fonte do frontend do projeto de portfólio, desenvolvido com React e Vite.

## Configuração e Execução

Para configurar e executar o frontend localmente, siga os passos abaixo:

1.  **Navegue até o diretório do frontend:**
    ```bash
    cd final_project/frontend
    ```

2.  **Instale as dependências:**
    ```bash
    npm install
    # ou yarn install
    # ou pnpm install
    ```

3.  **Inicie o servidor de desenvolvimento:**
    ```bash
    npm run dev
    # ou yarn dev
    # ou pnpm dev
    ```

O aplicativo estará disponível em `http://localhost:5173` (ou outra porta, dependendo da configuração do Vite).

## Estrutura do Projeto

O projeto segue uma estrutura padrão de aplicações React com Vite:

```
frontend/
├── public/                 # Arquivos estáticos
├── src/                    # Código-fonte da aplicação
│   ├── assets/             # Imagens e outros recursos
│   ├── components/         # Componentes React reutilizáveis
│   │   ├── LoginPage.jsx
│   │   ├── LoginPage.css
│   │   ├── ProfileImproved.jsx
│   │   ├── ProfileImproved.css
│   │   ├── MyHeader.jsx
│   │   ├── Carousel.jsx
│   │   └── ... (outros componentes)
│   ├── data/               # Dados estáticos (e.g., alunos.json, tags.json)
│   ├── hooks/              # Hooks personalizados (e.g., useAuth.js)
│   ├── services/           # Serviços para comunicação com a API (e.g., api.js)
│   ├── App.jsx             # Componente principal da aplicação e roteamento
│   ├── main.jsx            # Ponto de entrada da aplicação
│   └── index.css           # Estilos globais
├── .eslintrc.cjs
├── index.html
├── package.json
├── vite.config.js
└── ...
```

## Novas Funcionalidades e Alterações

### 1. Página de Login Dedicada

A página de login foi implementada como uma tela separada (`LoginPage.jsx`) com um design moderno e responsivo, baseada no modelo fornecido. Após o login bem-sucedido, o usuário é redirecionado para a página inicial (`/`).

-   **Localização:** `src/components/LoginPage.jsx` e `src/components/LoginPage.css`
-   **Funcionalidades:**
    -   Design visualmente aprimorado.
    -   Campo de senha com opção de mostrar/esconder.
    -   Opção "Continuar Conectado".
    -   Integração com o hook `useAuth` para autenticação via API.
    -   Redirecionamento para a página inicial após login.

### 2. Página de Perfil

Foi adicionada uma nova página de perfil (`ProfileImproved.jsx`) com um layout mais completo e funcionalidades de edição.

-   **Localização:** `src/components/ProfileImproved.jsx` e `src/components/ProfileImproved.css`
-   **Funcionalidades:**
    -   Exibição de informações do usuário (nome, nickname, bio, habilidades, projetos).
    -   Funcionalidade de edição de perfil (nome, nickname, bio, imagem de perfil, habilidades).
    -   Integração com `MyHeader` para navegação.
    -   Seção de projetos do usuário.

### 3. MyHeader (Cabeçalho)

O componente `MyHeader.jsx` foi atualizado para:

-   **Navegação da Logo:** Ao clicar na logo, o usuário é redirecionado para a página inicial (`/`).
-   **Integração de Login:** O botão `LOGIN` agora redireciona para a página de login (`/login`) se o usuário não estiver logado. Se estiver logado, o botão se torna `PERFIL` e redireciona para a nova página de perfil.
-   **Remoção de Elementos:** Elementos como a notificação de boas-vindas foram removidos para simplificar a interface.

### 4. Carousel

O componente `Carousel.jsx` foi ajustado para exibir os itens de 3 em 3. Se o último grupo de itens não completar 3, ele exibirá 1 ou 2 itens sem problemas, conforme solicitado.

### 5. Filtragem de Estudantes (SearchWindow e AlunoList)

A lógica de busca e filtragem de estudantes foi aprimorada:

-   **Compatibilidade de Tags:** Ao selecionar múltiplas tags na `SearchWindow`, o `AlunoList` agora exibirá apenas os estudantes que possuem **100% de compatibilidade** com todas as tags selecionadas em seus projetos. Ou seja, um estudante só será mostrado se tiver pelo menos um projeto que contenha *todas* as tags escolhidas.
-   **Busca por Termo:** A busca por termo (`searchTerm`) continua funcionando para filtrar por nome do estudante ou título do projeto.

## Roteamento

O roteamento da aplicação foi atualizado em `src/App.jsx`:

-   `/`: Página inicial com a lista de alunos e busca.
-   `/profile`: Nova página de perfil do usuário logado (`ProfileImproved`).
-   `/login`: Nova página de login dedicada (`LoginPage`).

## Considerações de Desenvolvimento

-   **Autenticação:** O sistema de autenticação utiliza JWT (JSON Web Tokens) para gerenciar sessões de usuário. O token é armazenado no `localStorage`.
-   **Estado Global:** O `useAuth` hook (`src/hooks/useAuth.js`) gerencia o estado de autenticação do usuário.
-   **API:** As requisições para o backend são feitas através da instância `axios` configurada em `src/services/api.js`.

## Testes

Recomenda-se realizar uma maratona de testes para validar todas as funcionalidades, desde o login até a busca por tags e a visualização do perfil.

---
