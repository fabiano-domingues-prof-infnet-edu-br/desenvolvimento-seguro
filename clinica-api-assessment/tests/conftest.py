import asyncio
import httpx
import pytest
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool

# 1. Importações dos modelos
from models.users import User
from models.patients import Patient
from models.appointments import Appointment

from database.connection import get_session
from main import app

# 2. Configurar banco em memória
test_engine = create_engine(
    "sqlite:///:memory:", 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

# 3. Criar as tabelas antes de qualquer teste rodar
SQLModel.metadata.create_all(test_engine)

def override_get_session():
    with Session(test_engine) as session:
        yield session

app.dependency_overrides[get_session] = override_get_session

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def default_client():
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
