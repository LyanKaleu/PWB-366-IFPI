from sqlmodel import create_engine, SQLModel


def get_engine():
    db_file_name = "todos.db"

    return create_engine(f"sqlite:///{db_file_name}")


def init_db():
    return SQLModel.metadata.create_all(get_engine())
