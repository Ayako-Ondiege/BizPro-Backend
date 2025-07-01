
### app/routes.py

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('routes', __name__)

@bp.route('/admin/dashboard')
@jwt_required()
def admin_dashboard():
    user = get_jwt_identity()
    if user['role'] != 'admin':
        return jsonify({"error": "Admins only"}), 403
    return jsonify({"message": f"Welcome Admin {user['id']}!"})

@bp.route('/customer/orders')
@jwt_required()
def customer_orders():
    user = get_jwt_identity()
    if user['role'] != 'customer':
        return jsonify({"error": "Customers only"}), 403
    return jsonify({"message": f"Welcome Customer {user['id']}!"})

@bp.route('/storekeeper/inventory')
@jwt_required()
def storekeeper_inventory():
    user = get_jwt_identity()
    if user['role'] != 'storekeeper':
        return jsonify({"error": "Storekeepers only"}), 403
    return jsonify({"message": f"Inventory for Storekeeper {user['id']}!"})

@bp.route('/supplier/portal')
@jwt_required()
def supplier_portal():
    user = get_jwt_identity()
    if user['role'] != 'supplier':
        return jsonify({"error": "Suppliers only"}), 403
    return jsonify({"message": f"Welcome Supplier {user['id']}!"})
