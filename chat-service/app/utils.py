# app/utils.py
import os
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordBearer
import requests

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str):
    auth_service_url = os.getenv("AUTH_SERVICE_URL", "http://localhost:8000")
    #print(token)
    response = requests.get(f"{auth_service_url}/validate-token", headers={"Authorization": f"Bearer {token}"})
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user_data = response.json()
    if "user_id" not in user_data:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user_data
