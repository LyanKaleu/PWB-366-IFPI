from sqlmodel import create_engine
from decouple import config


def get_engine():
    user = config('USER')
    password = config('PASSWORD')
    db_name = config('DB_NAME')
    host = config('HOST')
    port = config('PORT')
    
    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
