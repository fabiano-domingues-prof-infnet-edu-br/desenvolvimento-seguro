from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, sa_column_kwargs={"unique": True})
    password: str
    role: str = Field(default="recepcionista")

class UserSignIn(SQLModel):
    email: str
    password: str