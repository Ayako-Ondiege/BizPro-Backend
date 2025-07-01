import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = "super-secret"
    JWT_SECRET_KEY = "jwt-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///bizpro.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
