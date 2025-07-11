# backend/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env into environment variables

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-jwt-secret")

    # ✅ Prefer PostgreSQL if DATABASE_URL is defined, fallback to SQLite
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'bizpro.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
