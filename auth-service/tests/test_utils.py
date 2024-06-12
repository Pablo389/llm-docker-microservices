# tests/test_utils.py
import pytest
from datetime import timedelta
from app.utils import get_password_hash, verify_password, create_access_token, validate_token
from app.models import User, SessionLocal
from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")  # Esta clave debe coincidir con la clave utilizada en utils.py para pruebas
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100

@pytest.fixture
def db_session():
    # Configuración de la sesión de la base de datos para pruebas
    db = SessionLocal()
    yield db
    db.close()

def test_get_password_hash():
    password = "mysecretpassword"
    hashed_password = get_password_hash(password)
    assert hashed_password != password
    assert verify_password(password, hashed_password)

def test_verify_password():
    password = "mysecretpassword"
    hashed_password = get_password_hash(password)
    assert verify_password(password, hashed_password)
    assert not verify_password("wrongpassword", hashed_password)

def test_create_access_token():
    data = {"user_id": 1}
    token = create_access_token(data)
    decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded_data["user_id"] == 1

