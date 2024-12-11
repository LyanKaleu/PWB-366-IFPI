from sqlmodel import SQLModel, Field
from datetime import date, datetime


class TaskBase(SQLModel):
    title: str
    description: str
    done: bool = Field(default=False)
    created_at: str = Field(default=datetime.now().strftime('%Y-%m-%d'))
    due_date: date


class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key='user.id')


class RequestTask(TaskBase):
    pass


class UserBase(SQLModel):
    name: str
    email: str
    username: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str


class SignUpUserRequest(UserBase):
    password: str
    confirm_password: str


class SignInUserRequest(SQLModel):
    username: str
    password: str
