import time
from jose import jwt

# Chave secreta didática
SECRET_KEY = "chave_secreta_super_segura_para_estudantes"

def create_access_token(user: str):
    payload = {
        "user": user,
        "expires": time.time() + 3600
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_access_token(token: str):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        expire = data.get("expires")
        
        if expire is None or expire < time.time():
            return None
        return data
    except:
        return None