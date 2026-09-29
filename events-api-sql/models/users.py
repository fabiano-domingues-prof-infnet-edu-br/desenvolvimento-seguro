from typing import Optional
from pydantic import EmailStr
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "aluno@infnet.edu.br",
                "password": "password123",
            }
        }

class UserSignIn(SQLModel):
    email: EmailStr
    password: str