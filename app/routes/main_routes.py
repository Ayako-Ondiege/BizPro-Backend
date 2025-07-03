from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.utils.security import role_required

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the BizPro API 🚀"})

@bp.route("/admin-only", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def admin_only():
    return jsonify({"message": "Welcome, Admin!"})
