from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Criação da instância do FastAPI
app = FastAPI()


# Modelo de dados para representar um livro
class Livro(BaseModel):
    id: int | None = None # ID do livro, pode ser None para novos livros
    titulo: str # Título do livro	
    autor: str # Autor do livro
    genero: str # Gênero do livro
    ano_publicacao: int # Publicação do livro
    pais: str # País de origem do livro
    qtd_paginas: int # Quantidade de páginas do livro


# Criação de instâncias de livros
l1 = Livro(id=1, titulo="Ilíada e Odisséia", autor="Homero", genero="Épico", ano_publicacao=800, pais="Grécia", qtd_paginas=704)
l2 = Livro(id=2, titulo="Guerra e Paz", autor="Liev Tosltói", genero="Romance", ano_publicacao=1869, pais="Rússia", qtd_paginas=1440)
l3 = Livro(id=3, titulo="Orgulho e Preconceito", autor="Jane Austen", genero="Romance", ano_publicacao=1813, pais="Reino Unido", qtd_paginas=432)
l4 = Livro(id=4, titulo="Cem Anos de Solidão", autor="Gabriel García Márquez", genero="Romance", ano_publicacao=1967, pais="Colômbia", qtd_paginas=448)
l5 = Livro(id=5, titulo="Dom Quixote", autor="Miguel de Cervantes", genero="Romance", ano_publicacao=1605, pais="Espanha", qtd_paginas=1056)
l6 = Livro(id=6, titulo="O Senhor dos Anéis", autor="J. R. R. Tolkien", genero="Fantasia", ano_publicacao=1954, pais="Reino Unido", qtd_paginas=1200)
l7 = Livro(id=7, titulo="Crime e Castigo", autor="Fiódor Dostoiévski", genero="Romance", ano_publicacao=1866, pais="Rússia", qtd_paginas=576)
l8 = Livro(id=8, titulo="1984", autor="George Orwell", genero="Ficção Científica", ano_publicacao=1949, pais="Reino Unido", qtd_paginas=328)
l9 = Livro(id=9, titulo="O Apanhador no Campo de Centeio", autor="J. D. Salinger", genero="Romance", ano_publicacao=1951, pais="Estados Unidos", qtd_paginas=234)
l10 = Livro(id=10, titulo="Hamlet", autor="William Shakespeare", genero="Tragédia", ano_publicacao=1600, pais="Reino Unido", qtd_paginas=312)
l11 = Livro(id=11, titulo="O Pequeno Príncipe", autor="Antoine de Saint-Exupéry", genero="Fábula", ano_publicacao=1943, pais="França", qtd_paginas=96)
l12 = Livro(id=12, titulo="Romeu e Julieta", autor="William Shakespeare", genero="Tragédia", ano_publicacao=1600, pais="Reino Unido", qtd_paginas=240)


# Lista de livros
livros = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]


"""
-> FUNÇÃO DE LISTAR TODOS OS LIVROS:
Lista todos os livros, com opção de filtrar por gênero e ano de publicação.

- Gênero: parâmetro opcional para filtrar os livros por gênero.
- Ano de publicação: parâmetro opcional para filtrar os livros por ano de publicação.

Retorna uma lista de livros filtrados ou todos os livros se nenhum filtro for especificado.
"""
@app.get('/livros/')
def listar_livros(genero: str | None = None, ano_publicacao: int | None = None):
    livros_filtrados = []

    if genero:
        for livro in livros:
            if livro.genero == genero:
                livros_filtrados.append(livro)

    if ano_publicacao:
        for livro in livros:
            if livro.ano_publicacao == ano_publicacao:
                livros_filtrados.append(livro)

    if not genero and not ano_publicacao:
        return livros

    return livros_filtrados


"""
-> FUNÇÃO DE OBTER DETALHES DE UM LIVRO:
Retorna os detalhes de um livro específico pelo ID.

Retorna um HTTPException 404 se o livro não for encontrado.
"""
@app.get('/livros/{id}/')
def detalhes_livro(id: int):
    for livro in livros:
        if livro.id == id:
            return livro
    raise HTTPException(status_code=404, detail=f"Livro não encontrado com id = {id}")


"""
-> FUNÇÃO DE ADICIONAR UM LIVRO:
Adiciona um novo livro à lista.

- Livro: Objeto do tipo Livro a ser adicionado.

Retorna o livro adicionado.
"""
@app.post('/livros/')
def adicionar_livro(livro: Livro):
    livros.append(livro)
    return livro


"""
-> FUNÇÃO DE ATUALIZAR UM LIVRO:
Atualiza as informações de um livro específico pelo ID.

- ID: ID do livro a ser atualizado.
- Livro: Objeto do tipo Livro com as novas informações.

Lança uma exceção 404 se o livro não for encontrado.
"""
@app.put('/livros/{id}/')
def atualizar_livro(id: int, livro_atualizado: Livro):
    for livro in livros:
        if livro.id == id:
            livro.titulo = livro_atualizado.titulo
            livro.autor = livro_atualizado.autor
            livro.genero = livro_atualizado.genero
            livro.ano_publicacao = livro_atualizado.ano_publicacao
            livro.pais = livro_atualizado.pais
            livro.qtd_paginas = livro_atualizado.qtd_paginas
            return livro
    raise HTTPException(status_code=404, detail=f"Livro não encontrado com id = {id}")


"""
-> FUNÇÃO DE REMOVER UM LIVRO:
 Remove um livro específico da lista pelo ID.

 Lança uma exceção 404 se o livro não for encontrado.
"""
@app.delete('/livros/{id}/')
def remover_livro(id: int):
    for livro in livros:
        if livro.id == id:
            livros.remove(livro)
            return {"message": "Livro removido com sucesso"}
    raise HTTPException(status_code=404, detail=f"Livro não encontrado com id = {id}")
