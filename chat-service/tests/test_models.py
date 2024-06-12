# tests/test_chat_models.py
import pytest
from sqlalchemy.orm import Session
from app.models import Chat, Message

def test_create_chat(db_session: Session):
    chat = Chat(user_id=1)
    db_session.add(chat)
    db_session.commit()
    db_session.refresh(chat)
    
    assert chat.id is not None
    assert chat.user_id == 1
    assert chat.created_at is not None

def test_create_message(db_session: Session):
    chat = Chat(user_id=1)
    db_session.add(chat)
    db_session.commit()
    db_session.refresh(chat)
    
    message = Message(chat_id=chat.id, role="user", content="Hello, World!")
    db_session.add(message)
    db_session.commit()
    db_session.refresh(message)
    
    assert message.id is not None
    assert message.chat_id == chat.id
    assert message.role == "user"
    assert message.content == "Hello, World!"
    assert message.timestamp is not None
    assert message.chat.id == chat.id

def test_chat_messages_relationship(db_session: Session):
    chat = Chat(user_id=1)
    db_session.add(chat)
    db_session.commit()
    db_session.refresh(chat)
    
    message1 = Message(chat_id=chat.id, role="user", content="Hello, World!")
    message2 = Message(chat_id=chat.id, role="system", content="Hi, there!")
    db_session.add(message1)
    db_session.add(message2)
    db_session.commit()
    
    db_session.refresh(chat)
    assert len(chat.messages) == 2
    assert chat.messages[0].content == "Hello, World!"
    assert chat.messages[1].content == "Hi, there!"

