"""
utils.py - Utility functions for authentication service.

This module provides utility functions for password hashing, password verification,
JWT token creation, and token validation.
"""
import os
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
from app.models import User, SessionLocal

# Setup the password context for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key to encode JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "100"))

def get_password_hash(password: str) -> str:
    """
    Hashes the given password.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies that the plain password matches the hashed password.

    Args:
        plain_password (str): The plain password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Creates a JWT token.

    Args:
        data (dict): The data to include in the token.
        expires_delta (timedelta, optional): The time duration for the token to expire.

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def validate_token(token: str) -> dict:
    """
    Validates the given JWT token.

    Args:
        token (str): The JWT token to validate.

    Returns:
        dict: The decoded token data with user_id.

    Raises:
        JWTError: If the token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise JWTError("Invalid token")
        db = SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise JWTError("Invalid token")
        return {"user_id": user_id}
    except JWTError as exc:
        raise JWTError("Invalid token") from exc