# app/utils/security.py

from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify
from app.models import User

def role_required(allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if user and user.role in allowed_roles:
                return fn(*args, **kwargs)
            return jsonify({"error": "Unauthorized"}), 403
        return wrapper
    return decorator
