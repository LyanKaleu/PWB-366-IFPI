from fastapi import APIRouter, status, HTTPException, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlmodel import Session, select
from .models import *
from .database import get_engine
# from .security import *


router = APIRouter()


@router.post('/signup', response_model=UserBase)
async def signup(user_data: SignUpUserRequest):
    if user_data.password != user_data.confirm_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Passwords do not match')

    # Hash da senha
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    hashed_password = pwd_context.hash(user_data.password)

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


@router.post('/signin')
async def signin(login_data: SignInUserRequest):
    with Session(get_engine()) as session:
        # Pegar usuário por username
        sttm = select(User).where(User.username == login_data.username)
        user = session.exec(sttm).first()

        if not user:  # Não encontrou
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User or password incorrect')

        # Encontrou, então verificar a senha
        pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        valid = pwd_context.verify(login_data.password, user.password)

        if valid:
            return {'Token': 'Esse é seu crachá'}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User or password incorrect')

# @router.get('/', status_code=status.HTTP_200_OK)
# async def read_root():
#     return {'message': 'Hello World!'}
#
#
# @router.get('/users/')
# def read_users(
#         limit: int = 10, skip: int = 0, session: Session = Depends(get_engine),
#         current_user=Depends(get_current_user)
# ):
#     user = session.scalar(select(User).limit(limit).offset(skip))
#     return {'users': user}
#
#
# @router.post('/users/', status_code=status.HTTP_201_CREATED, response_model=User)
# async def create_user(user: User, session=Depends(get_engine)):
#     db_user = session.scalar(
#         select(User).where(
#             (User.username == user.username) | (User.email == user.email)
#         )
#     )
#
#     if db_user:
#         if db_user.username == user.username:
#             raise HTTPException(
#                 status_code=400, detail='Username already exists'
#             )
#         elif db_user.email == user.email:
#             raise HTTPException(
#                 status_code=400, detail='Email already exists'
#             )
#
#
# @router.put('/users/{user_id}', status_code=status.HTTP_200_OK)
# async def update_user(user_id: int, user: User, session: Session = Depends(get_engine), current_user=Depends(get_current_user)):
#     if current_user.id != user_id:
#         raise HTTPException(
#             status_code=400, detail='Not enough permissions'
#         )
#
#     current_user.name = user.name
#     current_user.username = user.username
#     current_user.email = user.email
#     current_user.password = get_password_hash(user.password)
#
#     session.commit()
#     session.refresh(current_user)
#
#     return current_user
#
#
# @router.post('/token', response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_engine)):
#     user = session.scalar(select(User).where(User.email == form_data.username))
#
#     if not user or not verify_password(form_data.password, user.password):
#         raise HTTPException(
#             status_code=400, detail='Incorrect username or password'
#         )
#
#     access_token = create_access_token(data={'sub': user.email})
#
#     return {'access_token': access_token, 'token_type': 'Bearer'}
#
#
# @router.delete('/users/{user_id}')
# def delete_user(
#         user_id: int, session: Session = Depends(get_engine),
#         current_user=Depends(get_current_user)
# ):
#     if current_user.id != user_id:
#         raise HTTPException(
#             status_code=400, detail='Not enough permissions'
#         )
#
#     session.delete(current_user)
#     session.commit()
#
#     return {'message': 'User deleted successfully'}
