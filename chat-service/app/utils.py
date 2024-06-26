"""
utils.py - Utility functions for chat service.

This module provides utility functions for token verification and interacting with OpenAI API.
"""

import os
import requests
from datetime import datetime, timedelta
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from openai import OpenAI

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str) -> dict:
    """
    Verifies the given token with the authentication service.

    Args:
        token (str): The token to verify.

    Returns:
        dict: The user data if the token is valid.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    auth_service_url = os.getenv("AUTH_SERVICE_URL", "http://localhost:8000")
    response = requests.get(f"{auth_service_url}/validate-token", headers={"Authorization": f"Bearer {token}"})
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user_data = response.json()
    if "user_id" not in user_data:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user_data

def get_openai_completion(user_msg: str) -> str:
    """
    Gets a completion from the OpenAI chat model based on the user message.

    Args:
        user_msg (str): The user message to send to the OpenAI chat model.

    Returns:
        str: The completion message from the OpenAI chat model.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=OPENAI_API_KEY)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_msg}
        ]
    )

    print(completion.choices[0].message)
    return completion.choices[0].message