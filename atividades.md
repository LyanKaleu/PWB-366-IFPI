## Atividades

- [API Books v1](https://github.com/LyanKaleu/PWB-366-IFPI/tree/main/2024-10-16)

> Crie uma API para gerenciar Livros. Faça as operações para:
> 
> - **Listar Todos**: Deve ser possível aplicar filtro por gênero e ano de lançamento.
> - **Obter Detalhes de um Livro por ID**.
> - **Atualizar Livro**.
> - **Remover Livro**.
> 
> Os atributos do Livro são:
> 
> - **id**: Identificador único do livro.
> - **titulo**: Título do livro.
> - **genero**: Gênero literário do livro.
> - **ano**: Ano de lançamento do livro.
> - **autor**: Autor do livro.
> - **pais**: País de origem do livro.
> - **quantidade de páginas**: Número de páginas do livro.

<br/><br/>
- [API Books v2](https://github.com/LyanKaleu/PWB-366-IFPI/tree/main/2024-11-05)

> Organize o código de acordo com o visto em sala de aula em Models, Controllers, Database e Main
> Use Banco de Dados SQL
> - Sugestão: Tente conectar com BD `PostgreSQL`


<br/><br/>
- [API - Tasks (Autenticação)](https://github.com/LyanKaleu/PWB-366-IFPI/tree/main/api_todo)
  
> Desenvolva uma API para gerenciamento de Tarefas (TODOs) usando FastAPI. Implemente operações para:
> 
> - **Criar Tarefa**: Enviar título, descrição e status de conclusão (opcional).
> - **Listar Todas**: Retornar todas as tarefas cadastradas.
> - **Obter Tarefa por ID**: Buscar uma tarefa específica pelo ID.
> - **Atualizar Tarefa**: Modificar título, descrição ou status de conclusão.
> - **Excluir Tarefa**: Deletar uma tarefa pelo ID.
> 
> Atributos das Tarefas:
> 
> - **id**: Identificador único.
> - **title**: Título da tarefa.
> - **description**: Descrição da tarefa.
> - **is_completed**: Status de conclusão (padrão: false).
> - **created_at**: Data e hora de criação.
> 
> Estrutura do Projeto:
> 
> - **Arquivos:** `main.py`, `models.py`, `controllers.py`.
> - **Banco de Dados:** SQLite ou PostgreSQL.
> - **Validações:** Utilize Pydantic para validar entradas.
> 
> **Dependências:**  
> FastAPI, SQLModel, Uvicorn.

<br/><br/>
- [Gestão de Projeto - Django Admin](https://github.com/LyanKaleu/PWB-366-IFPI/tree/main/django_projects/app_projetos)

> Objetivo: Criar um sistema de gerenciamento de projetos utilizando Django e o recurso Admin para gerenciar projetos, equipes, membros e atividades.
>
> ---
>
> Regras de Negócio:
>
> - **Um Projeto** tem **uma Equipe**.
> - **Uma Equipe** pode ter **vários Membros**.
> - **Um Projeto** pode ter **várias Atividades**.
> - **Uma Atividade** é realizada por **um Membro** da equipe do projeto.
>
> ---
>
> Etapas de Desenvolvimento
>
> 1. **Configuração do Projeto Django**
>    - Criar o projeto base.
>    - Configurar as dependências necessárias no ambiente.
>
> 2. **Criação do App Django**
>   - Criar um app específico para gerenciar os modelos.
>
> 3. **Criação do Superusuário**
>   - Criar um superusuário para gerenciar os registros no Admin.
>
> 4. **Criação dos Models**
>   - Definir os modelos necessários para:
>   - **Projetos**: Representar os projetos da empresa.
>   - **Equipes**: Representar os times que realizam os projetos.
>   - **Membros**: Representar os indivíduos que fazem parte das equipes.
>   - **Atividades**: Representar as tarefas relacionadas aos projetos.
>
> 5. **Migrações**
>   - Criar e aplicar as migrações para os modelos no banco de dados.
>
> 6. **Configuração do Admin**
>   - Ativar e configurar a interface do Django Admin para gerenciar os modelos.
>   - Implementar os **Inlines** para facilitar a gestão.
>
> ---
>
> Diagrama de Relacionamento
>```plaintext
>┌─────────────┐         ┌───────────┐
>│   Projeto   │ 1 ─── 1 │   Equipe  │
>└─────────────┘         └───────────┘
>       │ 1                   │ 1
>       │                     │
>       │                     ▼ *
>       │                ┌───────────┐
>       │                │   Membro  │
>       │                └───────────┘
>       │                     ▲ 1
>       │                     │
>       │         ┌───────────┘
>       ▼ *       |
>┌─────────────┐  │
>│  Atividade  │──┘*
>└─────────────┘


<br/><br/>
- [API Geek](https://github.com/LyanKaleu/PWB-366-IFPI/tree/main/django_projects/api_geek)
>
> Objetivo: Desenvolver uma API REST com Django/DRF que permita realizar operações básicas para um sistema de gerenciamento de vendas de artigos voltados para jovens de 13 a 19 anos. Os produtos são itens relacionados a séries, mangás/animes, games e cultura geek. A aplicação deve encapsular a lógica de negócio e banco de dados em uma classe de serviço, utilizando as técnicas abordadas em aula.
>
> Requisitos da Atividade:
> 1. **Estrutura do Projeto**:
>    - Utilize o framework Django/DRF.
>    - Implemente a organização de aplicações/módulos.
>    - Crie um banco de dados SQL simples utilizando o Models/Migrations para persistência dos dados.
>    - Crie Models, Views, URLS, Serializers e demais itens.
>
> 2. **Modelos**:
>    - **Produto**: Representa um item que está a venda na API.
>    - **Categoria**: Agrupamento de produto (e.g., Séries, Mangás, Games).
>    - **Franquia/Título**: Exemplo: "Naruto", "The Witcher", "Marvel".
>    - **Venda**: Representa a venda realizada.
>
> 3. **Funcionalidades CRUD**:
>    - **Criar Produto**: Endpoint para cadastrar um novo produto com atributos como nome, descrição, preço, estoque, categoria e franquia/título.
>    - **Listar Produtos**: Endpoint para retornar todos os produtos com filtros por nome, preço, categoria ou franquia.
>    - **Atualizar Produto**: Endpoint para atualizar as informações de um produto específico.
>    - **Atualizar Estoque Produto**: Endpoint para reposição ou venda de estoque.
>    - **Excluir Produto**: Endpoint para remover um produto com base em seu ID.
>    - **Vender Produto**: Cria uma venda com cliente, produto, quantidade e valor.
>    - **Repor Produto por ID**: Aumenta o estoque de um determinado produto.
>
> 4. **Relacionamentos**:
>    - O Atributo Categoria deve ser outro Model.
>    - O Atributo Franquia/Título deve ser também um Model.
>
> 5. **Regras de Negócio**:
>    - Produtos só podem ser excluídos se estiverem fora de estoque.
>    - Não é possível vender se não houver estoque.
>    - Reposição incrementa a quantidade de produtos.
>
> 6. **Admin**:
>    - Criação de painel administrativo para gestão dos produtos via Django Admin.
>
> 7. **Autenticação**:
>    - Autenticação com Token JWT.
>
> 8. **Busca, Filtro, Ordenação e Paginação**:
>    - Implemente recursos de busca, filtro, ordenação e paginação na API.
>
> 9. **Docs Swagger**:
>    - Ative o Swagger utilizando o pacote drf-yasg para documentação da API.
>
> 10. **Ferramentas de Teste**:
>    - Utilize Insomnia/Postman para testar os endpoints.
>
> **Avançando (Opcional)**:
> - **Perfil de Usuário**: Diferenciação entre vendedor e cliente, com permissões específicas para cada um.
>
> **Entrega**:
> - O código deve ser entregue via link para repositório Git ou arquivo ZIP até a data combinada.
> - (Opcional) Deploy no Render.com.

---
