from datetime import date, datetime
from sqlmodel import SQLModel, Field, Relationship


class UserBase(SQLModel):
    name: str
    email: str
    username: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str
    tasks: list["Task"] = Relationship(back_populates="user")


class SignUpUserRequest(UserBase):
    password: str
    confirm_password: str


class SignInUserRequest(SQLModel):
    username: str
    password: str


class TaskBase(SQLModel):
    title: str
    description: str
    done: bool = Field(default=False)
    created_at: str = Field(default=datetime.now().strftime('%Y-%m-%d'))
    due_date: date
    user_id: int | None = Field(default=None, foreign_key='user.id')


class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: User | None = Relationship(back_populates="tasks")


class TaskPublic(TaskBase):
    user: UserBase | None


class RequestTask(TaskBase):
    pass
