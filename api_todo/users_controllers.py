import jwt
from datetime import timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Annotated
from .models import *
from .database import get_engine
from .auth_utils import get_logged_user, gerar_hash, verificar_hash
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES


router = APIRouter()


@router.post('/signup', response_model=UserBase)
async def signup(user_data: SignUpUserRequest):
    if user_data.password != user_data.confirm_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Passwords do not match')

    # Hash da senha
    hashed_password = gerar_hash(user_data.password)

    user = User(
        email=user_data.email,
        username=user_data.username,
        name=user_data.name,
        password=hashed_password
    )

    with Session(get_engine()) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        return user


@router.post('/signin', response_model=dict)
async def signin(login_data: SignInUserRequest):
    with Session(get_engine()) as session:
        # Pegar usuário por username
        sttm = select(User).where(User.username == login_data.username)
        user = session.exec(sttm).first()

        if not user:  # Não encontrou
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User or password incorrect')

        # Encontrou, então verificar a senha
        valid = verificar_hash(login_data.password, user.password)

        if valid:
            expires_at = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = jwt.encode({'sub': user.username, 'exp': expires_at}, SECRET_KEY, algorithm=ALGORITHM)

            expires_rt = datetime.now(timezone.utc) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
            refresh_token = jwt.encode({'sub': user.username, 'exp': expires_rt}, SECRET_KEY, algorithm=ALGORITHM)

            return {'access_token': access_token, 'refresh_token': refresh_token}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User or password incorrect')


@router.get('/me', response_model=UserBase)
async def me(user: Annotated[User, Depends(get_logged_user)]):
    return user
