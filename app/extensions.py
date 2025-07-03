
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate  # ✅ ensure this is here

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()  # ✅ add this line