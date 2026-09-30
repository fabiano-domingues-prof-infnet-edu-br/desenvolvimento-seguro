from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from database.connection import get_session
from models.users import User
from auth.authenticate import authenticate

class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, email: str = Depends(authenticate), session: Session = Depends(get_session)) -> User:
        user = session.exec(select(User).where(User.email == email)).first()
        
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")
            
        if user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail=f"Acesso negado. Seu perfil ({user.role}) não tem permissão para esta ação."
            )
        
        return user # Retorna o objeto do usuário logado e validado
