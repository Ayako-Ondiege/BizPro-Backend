from flask import Flask
from app.extensions import db, jwt, migrate
from app.routes.auth_routes import auth_bp
from app.routes.main_routes import bp as routes_bp
from app import models  # Ensure models are registered for migrations

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(routes_bp)

    return app

# ✅ Make create_app accessible for seed.py and CLI
create_app = create_app
