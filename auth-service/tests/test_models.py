# tests/test_models.py

from app.models import User
import pytest

def test_create_user(db_session):
    # Crear un nuevo usuario
    new_user = User(email="test@example.com", hashed_password="hashedpassword123")
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    
    # Verificar que el usuario fue creado correctamente
    assert new_user.id is not None
    assert new_user.email == "test@example.com"
    assert new_user.hashed_password == "hashedpassword123"

def test_read_user(db_session):
    # Crear un nuevo usuario
    new_user = User(email="test2@example.com", hashed_password="hashedpassword456")
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    
    # Leer el usuario de la base de datos
    user_from_db = db_session.query(User).filter_by(email="test2@example.com").first()
    
    # Verificar que el usuario fue leído correctamente
    assert user_from_db is not None
    assert user_from_db.email == "test2@example.com"
    assert user_from_db.hashed_password == "hashedpassword456"

def test_create_duplicate_user_email(db_session):
    # Crear el primer usuario
    user1 = User(email="duplicate@example.com", hashed_password="password123")
    db_session.add(user1)
    db_session.commit()
    db_session.refresh(user1)
    
    # Intentar crear un segundo usuario con el mismo email
    user2 = User(email="duplicate@example.com", hashed_password="password456")
    db_session.add(user2)
    
    # Verificar que se lanza una excepción al intentar guardar el segundo usuario
    with pytest.raises(Exception) as excinfo:
        db_session.commit()
    
    # Comprobar que la excepción se debe a la violación de la unicidad del email
    assert "UNIQUE constraint failed: users.email" in str(excinfo.value)