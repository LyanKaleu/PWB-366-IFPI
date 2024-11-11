from fastapi import APIRouter, status, HTTPException
from .models import *
from sqlmodel import Session, select
from .database import get_engine


router = APIRouter()

clubes: list[Clube] = []
clube1 = Clube(id=1, nome='Flamengo', serie='A')
clubes.append(clube1)
clubes.append(Clube(id=2, nome='Corinthians', serie='A'))
clubes.append(Clube(id=3, nome='Santos', serie='B'))


@router.get("", status_code=status.HTTP_200_OK)
def get_clubes(serie: str | None = None):
    session = Session(get_engine())

    statement = select(Clube)

    if serie:
        statement = statement.where(Clube.serie == serie)

    clubes_fut = session.exec(statement).all()

    return clubes_fut


@router.get("/{clube_id}")
def detalhes_clube(clube_id: int):
    with Session(get_engine()) as session:
        statement = select(Clube).where(Clube.id == clube_id)
        clube = session.exec(statement).one_or_none()
        
        if clube:
            return clube

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Clube não encontrado com id = {clube_id}")


@router.post("", status_code=status.HTTP_201_CREATED)
def add_clube(request_clube: RequestClube):
    session = Session(get_engine())
    request_clube = Clube(nome=request_clube.nome, serie=request_clube.serie)
    session.add(request_clube)
    session.commit()
    session.refresh(request_clube)

    return request_clube


@router.put("/{clube_id}")
def update_clube(clube_id: int, dados: RequestClube):
    with Session(get_engine()) as session:
        statement = select(Clube).where(Clube.id == clube_id)
        clube = session.exec(statement).one_or_none()
        
        if clube:
            clube.nome = dados.nome
            clube.serie = dados.serie
            session.add(clube)
            session.commit()
            session.refresh(clube)
            return clube
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Clube não encontrado com id = {clube_id}"
    )

@router.delete("/{clube_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_clube(clube_id: int):
    with Session(get_engine()) as session:
        statement = select(Clube).where(Clube.id == clube_id)
        clube = session.exec(statement).one_or_none()

        if clube:
            session.delete(clube)
            session.commit()
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Clube não encontrado com id = {clube_id}"
    )
