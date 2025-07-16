from flask import Flask
from app.extensions import db, jwt, migrate
from app.routes.api import register_api_routes
from app.routes.auth_routes import auth_bp   # ✅ Add this line
from app import models

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    register_api_routes(app)          # RESTful routes
    app.register_blueprint(auth_bp)   # ✅ Register auth routes (login/register)

    return app

create_app = create_app
