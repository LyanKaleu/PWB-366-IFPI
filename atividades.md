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


- [API Books v2](https://github.com/LyanKaleu/PWB-366-IFPI/tree/main/2024-11-05)

> Organize o código de acordo com o visto em sala de aula em Models, Controllers, Database e Main
> Use Banco de Dados SQL
> - Sugestão: Tente conectar com BD `PostgreSQL`


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

-[Gestão de Projeto - Django Admin](https://github.com/LyanKaleu/PWB-366-IFPI/tree/main/django_projects/app_projetos)

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
> --
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
```plaintext
┌─────────────┐         ┌───────────┐
│   Projeto   │ 1     1 │   Equipe  │
└─────────────┘         └───────────┘
       │ 1                   │ 1
       │                     │
       │                     ▼ *
       │                ┌───────────┐
       │                │   Membro  │
       │                └───────────┘
       │                     ▲ 1
       │                     │
       │         ┌───────────┘
       ▼ *       │
┌─────────────┐  │
│  Atividade  │──┘*
└─────────────┘