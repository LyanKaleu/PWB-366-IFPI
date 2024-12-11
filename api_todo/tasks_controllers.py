from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlmodel import Session, select
from .auth_utils import get_logged_user
from .models import *
from .database import get_engine


router = APIRouter()


@router.post("", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(request_task: RequestTask, user: Annotated[User, Depends(get_logged_user)]):
    valid_task = Task.model_validate(request_task)
    valid_task.user_id = user.id

    with Session(get_engine()) as session:
        existing_task = session.exec(
            select(Task).where(Task.title == valid_task.title,
                               Task.description == valid_task.description,
                               Task.user_id == user.id)
        ).first()

        if existing_task:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task already exists")

        session.add(valid_task)
        session.commit()
        session.refresh(valid_task)

        return valid_task


@router.get("", response_model=list[Task], status_code=status.HTTP_200_OK)
async def get_all_tasks():
    with Session(get_engine()) as session:
        tasks = session.exec(select(Task)).all()

        return tasks


@router.get("/{task_id}", response_model=Task, status_code=status.HTTP_200_OK)
async def get_task_by_id(task_id: int, user: Annotated[User, Depends(get_logged_user)]):
    with Session(get_engine()) as session:
        statement = select(Task).where(Task.id == task_id, Task.user_id == user.id)
        task = session.exec(statement).one_or_none()

        if task:
            return task

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task not found with id = {task_id}")


@router.put("/{task_id}", response_model=Task, status_code=status.HTTP_200_OK)
async def update_task(task_id: int, request_task: RequestTask, user: Annotated[User, Depends(get_logged_user)]):
    with Session(get_engine()) as session:
        statement = select(Task).where(Task.id == task_id, Task.user_id == user.id)
        task = session.exec(statement).one_or_none()

        if task:
            task.title = request_task.title
            task.description = request_task.description
            session.add(task)
            session.commit()
            session.refresh(task)

            return task

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task not found with id = {task_id}")


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, user: Annotated[User, Depends(get_logged_user)]):
    with Session(get_engine()) as session:
        statement = select(Task).where(Task.id == task_id, Task.user_id == user.id)
        task = session.exec(statement).first()

        if task:
            session.delete(task)
            session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task not found with id = {task_id}")


@router.post("/{task_id}/done", response_model=Task, status_code=status.HTTP_200_OK)
async def task_mark_as_done(task_id: int, user: Annotated[User, Depends(get_logged_user)]):
    with Session(get_engine()) as session:
        statement = select(Task).where(Task.id == task_id, Task.user_id == user.id)
        task = session.exec(statement).first()

        if task:
            task.done = True
            session.add(task)
            session.commit()
            session.refresh(task)

            return task

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task not found with id = {task_id}")
