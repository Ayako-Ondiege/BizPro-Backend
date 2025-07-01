### app/__init__.py

from flask import Flask
from app.extensions import db, jwt
from app.auth import auth_bp
from app.routes import bp as routes_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(routes_bp)

    return app

