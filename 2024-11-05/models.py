from sqlmodel import SQLModel, Field


class LivroBase(SQLModel):
    titulo: str 
    autor: str 
    genero: str 
    ano_publicacao: int 
    pais: str 
    qtd_paginas: int


class Livro(LivroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class RequestLivro(LivroBase):
    pass
