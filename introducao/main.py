from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

class Clube(BaseModel):
    id: int | None = None
    nome: str = Field(min_length=3)
    serie: str = Field(min_length=1, max_length=1)

class AlterarClube(BaseModel):
    nome: str = Field(min_length=3)
    serie: str = Field(min_length=1, max_length=1)


clubes: list[Clube] = []

clube1 = Clube(id=1, nome='Flamengo', serie='A')
clubes.append(clube1)
clubes.append(Clube(id=2, nome='Corinthians', serie='A'))
clubes.append(Clube(id=3, nome='Santos', serie='B'))


@app.get("/clubes", status_code=status.HTTP_200_OK)
def get_clubes(serie: str | None = None):
    if not serie:
        return clubes

    clubes_fut = []
    for clube in clubes:
        if clube.serie == serie:
            clubes_fut.append(clube)
    return clubes_fut


@app.get("/clubes/{clube_id}")
async def detalhes_clube(clube_id: int):
    for clube in clubes:
        if clube_id == clube.id:
            return clube

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Clube não encontrado com id = {clube_id}")


@app.post("/clubes", status_code=status.HTTP_201_CREATED)
def add_clube(novo_clube: Clube):
    clubes.append(novo_clube)
    return novo_clube


@app.put("/clubes/{clube_id}")
def update_clube(clube_id: int, dados: AlterarClube):
    for clube in clubes:
        if clube.id == clube_id:
            clube.nome = dados.nome
            return clube
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Clube não encontrado com id = {clube_id}"
    )

@app.delete("/clubes/{clube_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_clube(clube_id: int):
    for clube in clubes:
        if clube.id == clube_id:
            clubes.remove(clube)
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Clube não encontrado com id = {clube_id}"
    )
