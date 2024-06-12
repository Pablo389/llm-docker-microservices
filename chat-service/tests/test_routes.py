import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app import app
from app.models import init_db, SessionLocal

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    init_db()
    yield SessionLocal()

@pytest.fixture
def token():
    return "valid_token"

def mock_verify_token(token: str):
    return {"user_id": 1, "email": "test@example.com"}

@patch("app.routes.verify_token", side_effect=mock_verify_token)
def test_create_chat(mock_verify, db, token):
    response = client.post("/create-chat", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 1
    assert "id" in data
