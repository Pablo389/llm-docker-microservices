# app/routes.py
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas import ChatCreate, MessageCreate, Chat, Message
from app.models import Chat as DBChat, Message as DBMessage, SessionLocal
from app.utils import verify_token
from typing import List
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create-chat", response_model=Chat)
def create_chat(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    #print(token)
    token_new = verify_token(token)
    user_id = token_new["user_id"]
    new_chat = DBChat(user_id=user_id)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat

@router.post("/create-message", response_model=Message)
def create_message(message: MessageCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_new = verify_token(token)
    user_id = token_new["user_id"]
    new_message = DBMessage(chat_id=message.chat_id, role=message.role, content=message.content)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

@router.get("/chats", response_model=List[Chat])
def get_chats(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_new = verify_token(token)
    user_id = token_new["user_id"]
    chats = db.query(DBChat).filter(DBChat.user_id == user_id).all()
    return chats

@router.get("/messages/{chat_id}", response_model=List[Message])
def get_messages(chat_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_new = verify_token(token)
    user_id = token_new["user_id"]
    messages = db.query(DBMessage).filter(DBMessage.chat_id == chat_id).all()
    return messages