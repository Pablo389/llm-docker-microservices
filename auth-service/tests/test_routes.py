# tests/test_routes.py
import pytest
from fastapi.testclient import TestClient
from app import app  # Asegúrate de que 'app' esté importado desde el archivo correcto
from app.models import User, SessionLocal
from app.utils import get_password_hash

client = TestClient(app)

@pytest.fixture
def db_session():
    # Configuración de la sesión de la base de datos para pruebas
    db = SessionLocal()
    yield db
    db.close()



def test_register_existing_user():
    # Intentar registrar el mismo usuario nuevamente
    response = client.post("/register", json={"email": "testuser4@example.com", "password": "password123"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

def test_login_user():
    response = client.post("/login", json={"email": "testuser4@example.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_user():
    response = client.post("/login", json={"email": "invaliduser@example.com", "password": "password123"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid credentials"}

def test_validate_token():
    login_response = client.post("/login", json={"email": "testuser4@example.com", "password": "password123"})
    token = login_response.json()["access_token"]
    validate_response = client.get("/validate-token", headers={"Authorization": f"Bearer {token}"})
    assert validate_response.status_code == 200
    assert "user_id" in validate_response.json()

def test_validate_invalid_token():
    validate_response = client.get("/validate-token", headers={"Authorization": "Bearer invalidtoken"})
    assert validate_response.status_code == 401
    assert "detail" in validate_response.json()