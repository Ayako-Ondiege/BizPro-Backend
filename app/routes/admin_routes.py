# app/routes/admin_routes.py

from flask import request, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required
from app.utils.security import role_required
from app.extensions import db
from app.models import User

# ✅ Create a Blueprint
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")
api = Api(admin_bp)

# ✅ Define the resources
class UserListResource(Resource):
    @jwt_required()
    @role_required(["admin"])
    def get(self):
        users = User.query.all()
        return [
            {
                "id": u.id,
                "username": u.username,
                "email": u.email,
                "role": u.role
            } for u in users
        ], 200


class AdminCreateUserResource(Resource):
    @jwt_required()
    @role_required(["admin"])
    def post(self):
        data = request.get_json()
        required_fields = ("username", "email", "password", "role")
        if not all(k in data for k in required_fields):
            return {"error": "All fields are required"}, 400

        if User.query.filter_by(username=data["username"]).first():
            return {"error": "Username already exists"}, 400
        if User.query.filter_by(email=data["email"]).first():
            return {"error": "Email already exists"}, 400

        new_user = User(
            username=data["username"],
            email=data["email"],
            role=data["role"]
        )
        new_user.set_password(data["password"])
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully"}, 201


class PromoteUserResource(Resource):
    @jwt_required()
    @role_required(["admin"])
    def patch(self, user_id):
        data = request.get_json()
        new_role = data.get("role")
        if not new_role:
            return {"error": "New role is required"}, 400

        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        user.role = new_role
        db.session.commit()

        return {"message": f"User promoted to {new_role}"}, 200


class DeleteUserResource(Resource):
    @jwt_required()
    @role_required(["admin"])
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200

# ✅ Register resources with the API
api.add_resource(UserListResource, "/users")
api.add_resource(AdminCreateUserResource, "/create-user")
api.add_resource(PromoteUserResource, "/promote/<int:user_id>")
api.add_resource(DeleteUserResource, "/delete/<int:user_id>")

