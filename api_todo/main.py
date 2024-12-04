from fastapi import FastAPI
from .tasks_controllers import router as task_router
from .users_controllers import router as user_router
from .database import init_db


app = FastAPI()


app.include_router(task_router, prefix="/tasks")
app.include_router(user_router, prefix="/users")

# Criar DB
init_db()
