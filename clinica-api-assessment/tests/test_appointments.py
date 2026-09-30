import pytest
import httpx
from sqlmodel import Session
from models.users import User
from auth.hash_password import HashPassword
from tests.conftest import test_engine

hasher = HashPassword()

@pytest.fixture(scope="module")
async def setup_users(default_client: httpx.AsyncClient):
    # Criando os usuários diretamente no banco de teste
    recepcionista = User(name="Ana", email="ana@clinica.com", password=hasher.create_hash("123"), role="recepcionista")
    medico = User(name="Dr. House", email="house@clinica.com", password=hasher.create_hash("123"), role="profissional")
    
    with Session(test_engine) as session:
        session.add(recepcionista)
        session.add(medico)
        session.commit()

@pytest.mark.asyncio
async def test_medico_nao_pode_criar_consulta(default_client: httpx.AsyncClient, setup_users):
    # 1. Faz login como médico
    login_response = await default_client.post("/user/signin", json={"email": "house@clinica.com", "password": "123"})
    token = login_response.json().get("access_token")
    
    # 2. Tenta agendar (Deve ser barrado)
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "patient_id": 1,
        "professional_id": 2,
        "date_time": "2026-10-10T10:00:00",
        "notes": "Rotina"
    }
    
    response = await default_client.post("/appointment/new", json=payload, headers=headers)
    
    assert response.status_code == 403
    assert "Acesso negado" in response.json()["detail"]

@pytest.mark.asyncio
async def test_recepcionista_pode_criar_consulta(default_client: httpx.AsyncClient, setup_users):
    # 1. Faz login como recepcionista
    login_response = await default_client.post("/user/signin", json={"email": "ana@clinica.com", "password": "123"})
    token = login_response.json().get("access_token")
    
    # Obs: Num cenário real precisaríamos inserir um paciente no banco primeiro
    # O foco deste teste é apenas provar que o RBAC libera a rota (não retorna 403)
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "patient_id": 1, 
        "professional_id": 2,
        "date_time": "2026-10-10T10:00:00"
    }
    
    response = await default_client.post("/appointment/new", json=payload, headers=headers)
    
    # Como o paciente_id=1 não existe ainda no DB, o banco vai dar erro de chave estrangeira,
    # Mas o importante é que NÃO é um erro 403 (Forbidden), provando que passou pelo RoleChecker
    assert response.status_code != 403