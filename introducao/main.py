from fastapi import FastAPI
from sqlmodel import SQLModel
from .clubes_controller import router as clubes_router
from .database import get_engine

# Passos
# > pip install -r requirements.txt
# > fastapi dev main.py

app = FastAPI()

# Registrar os Router (controllers)
app.include_router(clubes_router, prefix="/clubes")

# Criar DB
SQLModel.metadata.create_all(get_engine())
