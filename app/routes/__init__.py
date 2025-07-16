# app/routes/__init__.py

from flask import Blueprint
from flask_restful import Api

# Import all Supplier routes
from app.routes.supplier_routes import SupplierListResource, SupplierResource
from app.routes.admin_routes import (
    UserListResource,
    AdminCreateUserResource,
    PromoteUserResource,
    DeleteUserResource
)
from app.routes.auth_routes import auth_bp

# Setup Blueprint and Flask-RESTful API
api_bp = Blueprint("api", __name__, url_prefix="/")
api = Api(api_bp)

# Supplier Routes
api.add_resource(SupplierListResource, "/suppliers")
api.add_resource(SupplierResource, "/suppliers/<int:id>")  # ✅ Add this line

# Admin Routes
api.add_resource(UserListResource, "/admin/users")
api.add_resource(AdminCreateUserResource, "/admin/create-user")
api.add_resource(PromoteUserResource, "/admin/users/<int:user_id>/promote")
api.add_resource(DeleteUserResource, "/admin/users/<int:user_id>")

# Register auth blueprint
api_bp.register_blueprint(auth_bp)

__all__ = ["api_bp"]
