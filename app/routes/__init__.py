# app/routes/__init__.py

from flask import Blueprint
from flask_restful import Api

# Flask-RESTful Resource Classes
from app.routes.supplier_routes import SupplierListResource
from app.routes.admin_routes import (
    UserListResource,
    AdminCreateUserResource,
    PromoteUserResource,
    DeleteUserResource
)

# Traditional Flask Blueprint Routes (auth)
from app.routes.auth_routes import auth_bp

# Initialize API blueprint and RESTful API wrapper
api_bp = Blueprint("api", __name__, url_prefix="/")
api = Api(api_bp)

# ========================
# Register Flask-RESTful Routes
# ========================

# Supplier Resource Routes
api.add_resource(SupplierListResource, "/suppliers")

# Admin Resource Routes
api.add_resource(UserListResource, "/admin/users")
api.add_resource(AdminCreateUserResource, "/admin/create-user")
api.add_resource(PromoteUserResource, "/admin/users/<int:user_id>/promote")
api.add_resource(DeleteUserResource, "/admin/users/<int:user_id>")

# ========================
# Register traditional (non-resource) auth routes
# ========================
api_bp.register_blueprint(auth_bp)

# Export to be used in app/__init__.py
__all__ = ["api_bp"]

