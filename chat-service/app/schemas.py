# app/schemas.py
from pydantic import BaseModel
from typing import List
from datetime import datetime

class MessageCreate(BaseModel):
    chat_id: int
    role: str
    content: str

    class Config:
        orm_mode = True

class Message(BaseModel):
    id: int
    chat_id: int
    role: str
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True

class ChatCreate(BaseModel):
    user_id: int

class Chat(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    messages: List[Message] = []

    class Config:
        orm_mode = True