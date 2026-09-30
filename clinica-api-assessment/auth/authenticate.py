from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")

async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token ausente")
        
    decoded_token = verify_access_token(token)
    if not decoded_token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token inválido ou expirado")
        
    return decoded_token["user"]  # Retorna o email do usuário