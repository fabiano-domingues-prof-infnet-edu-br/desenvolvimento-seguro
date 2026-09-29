from typing import Optional, List
from sqlmodel import JSON, SQLModel, Field, Column

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "Evento Infnet",
                "image": "https://infnet.edu.br",
                "description": "Apresentação do Curso",
                "tags": ["curso", "dev", "seguro"],
                "location": "Zoom"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]