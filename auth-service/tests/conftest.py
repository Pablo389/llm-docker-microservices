# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User

DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="module")
def engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    return engine

@pytest.fixture(scope="module")
def Session(engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal

@pytest.fixture(scope="function")
def db_session(Session):
    session = Session()
    yield session
    session.close()
