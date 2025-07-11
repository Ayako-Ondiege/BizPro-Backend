# app/__init__.py

from flask import Flask
from app.extensions import db, jwt, migrate
from app import models  # Ensure models are imported for migrations

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Import and register routes after initializing extensions
    from app.routes import api_bp
    app.register_blueprint(api_bp)

    return app

# Make factory accessible to CLI and seed scripts
create_app = create_app
