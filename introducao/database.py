from sqlmodel import create_engine
from decouple import config


def get_engine():
    # Usuário e Senha
    user = config('USER')
    password = config('PASSWORD')
    # Nome do Banco de Dados
    db_name = config('DB_NAME')
    # Host e Porta
    host = config('HOST')
    port = config('PORT')
    # Montar a URL para conexão
    url = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    return create_engine(url)