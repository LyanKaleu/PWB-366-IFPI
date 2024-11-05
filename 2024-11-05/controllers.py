from fastapi import APIRouter, status, HTTPException

from .database import get_engine
from .models import Livro, RequestLivro
from sqlmodel import Session, select


router = APIRouter()


@router.get('', status_code=status.HTTP_200_OK)
def listar_livros(genero: str | None = None, ano_publicacao: int | None = None):
    session = Session(get_engine())

    statement = select(Livro)

    if genero:
        statement = statement.where(Livro.genero == genero)

    if ano_publicacao:
        statement = statement.where(Livro.ano_publicacao == ano_publicacao)
    
    if genero and ano_publicacao:
        statement = statement.where(Livro.genero == genero).where(Livro.ano_publicacao == ano_publicacao)
    
    livros = session.exec(statement).all()

    return livros


@router.get('/{id}', status_code=status.HTTP_200_OK)
def detalhes_livro(id: int):
    session = Session(get_engine())

    statement = select(Livro).where(Livro.id == id)
    livro = session.exec(statement).first()
    
    if livro is None:
        raise HTTPException(status_code=404, detail=f"Livro não encontrado com id = {id}")
    
    return livro


@router.post('', status_code=status.HTTP_201_CREATED)
def adicionar_livro(request_livro: RequestLivro):
    livro = Livro(
        titulo=request_livro.titulo,
        autor=request_livro.autor,
        genero=request_livro.genero,
        ano_publicacao=request_livro.ano_publicacao,
        pais=request_livro.pais,
        qtd_paginas=request_livro.qtd_paginas,
    )

    session = Session(get_engine())
    session.add(livro)
    session.commit()
    session.refresh(livro)

    return livro


@router.put('/{id}', status_code=status.HTTP_200_OK)
def atualizar_livro(id: int, livro_atualizado: Livro):
    session = Session(get_engine())
    
    statement = select(Livro).where(Livro.id == id)
    livro = session.exec(statement).first()
    
    
    if livro is None:
        raise HTTPException(status_code=404, detail=f"Livro não encontrado com id = {id}")
    
    livro.titulo = livro_atualizado.titulo
    livro.autor = livro_atualizado.autor
    livro.genero = livro_atualizado.genero
    livro.ano_publicacao = livro_atualizado.ano_publicacao
    livro.pais = livro_atualizado.pais
    livro.qtd_paginas = livro_atualizado.qtd_paginas
    
    session.commit()
    
    return livro


@router.delete('/livros/{id}/', status_code=status.HTTP_204_NO_CONTENT)
def remover_livro(id: int):
    session = Session(get_engine())

    statement = select(Livro).where(Livro.id == id)
    livro = session.exec(statement).first()
    
    if livro is None:
        raise HTTPException(status_code=404, detail=f"Livro não encontrado com id = {id}")
    
    session.delete(livro)
    session.commit()
