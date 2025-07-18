# app/routes/__init__.py

# app/routes/__init__.py

from flask import Blueprint
from flask_restful import Api

# Import Supplier routes
from app.routes.supplier_routes import SupplierListResource, SupplierResource

# Import Auth Blueprint (already using a blueprint for auth)
from app.routes.auth_routes import auth_bp

# Setup Blueprint and Flask-RESTful API
api_bp = Blueprint("api", __name__, url_prefix="/")
api = Api(api_bp)

# ✅ Supplier Routes
api.add_resource(SupplierListResource, "/suppliers")
api.add_resource(SupplierResource, "/suppliers/<int:id>")

# ✅ Register Auth Blueprint
api_bp.register_blueprint(auth_bp)

__all__ = ["api_bp"]

