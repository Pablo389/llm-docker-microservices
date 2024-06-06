# app/__init__.py
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

from app import routes

app.include_router(routes.router)
