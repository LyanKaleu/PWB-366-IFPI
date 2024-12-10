from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlmodel import Session, select
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from .database import get_engine
from .models import User
import jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def gerar_hash(texto):
    return pwd_context.hash(texto)


def verificar_hash(texto, hash_pwd):
    return pwd_context.verify(texto, hash_pwd)


def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt


def verificar_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return payload.get('sub')


async def get_logged_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # Pegar o Token na Request, se válido pegará o usuário do BD para confirmar e retornar ele

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')

    try:
        username = verificar_access_token(token)
    except jwt.PyJWTError:
        raise exception


    if not username:
        raise exception

    with Session(get_engine()) as session:
        sttm = select(User).where(User.username == username)
        user = session.exec(sttm).first()

        if not user:
            raise exception

        return user
