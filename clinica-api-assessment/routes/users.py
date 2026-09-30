from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database.connection import get_session
from models.users import User, UserSignIn
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token

user_router = APIRouter(tags=["Users"])
hash_password = HashPassword()

@user_router.post("/signup")
async def sign_user_up(user: User, session: Session = Depends(get_session)):
    user_exist = session.exec(select(User).where(User.email == user.email)).first()
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email já cadastrado.")
    
    user.password = hash_password.create_hash(user.password)
    session.add(user)
    session.commit()
    return {"message": "Usuário criado com sucesso!"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn, session: Session = Depends(get_session)):
    user_exist = session.exec(select(User).where(User.email == user.email)).first()
    
    if not user_exist or not hash_password.verify_hash(user.password, user_exist.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas.")
        
    access_token = create_access_token(user_exist.email)
    return {"access_token": access_token, "token_type": "Bearer"}
