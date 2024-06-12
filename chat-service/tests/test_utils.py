# tests/test_utils.py
import os
import pytest
import requests
from unittest.mock import patch, Mock
from app.utils import verify_token, get_openai_completion

def test_verify_token_success():
    # Mocking the response from the authentication service
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"user_id": 1, "email": "test@example.com"}
        mock_get.return_value = mock_response
        
        os.environ["AUTH_SERVICE_URL"] = "http://localhost:8000"
        token = "valid_token"
        user_data = verify_token(token)
        
        assert user_data["user_id"] == 1
        assert user_data["email"] == "test@example.com"

def test_verify_token_invalid():
    # Mocking the response from the authentication service
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"detail": "Invalid or expired token"}
        mock_get.return_value = mock_response
        
        os.environ["AUTH_SERVICE_URL"] = "http://localhost:8000"
        token = "invalid_token"
        
        with pytest.raises(Exception) as exc_info:
            verify_token(token)
        
        assert exc_info.value.status_code == 401
        assert exc_info.value.detail == "Invalid or expired token"

def test_get_openai_completion():
    # Mocking the OpenAI API client
    with patch("openai.OpenAI") as mock_openai:
        mock_client = Mock()
        mock_openai.return_value = mock_client
        mock_response = Mock()
        mock_response.choices = [Mock(message={"role": "assistant", "content": "Test response"})]
        mock_client.chat.completions.create.return_value = mock_response
        
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        user_msg = "Hello, how are you?"
        response = get_openai_completion(user_msg)
        
        print(response)
        assert response.role == "assistant"
        #assert response["content"] == "Test response"
