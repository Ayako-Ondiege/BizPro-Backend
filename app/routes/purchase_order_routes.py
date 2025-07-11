# app/routes/purchase_order_routes.py (Flask-RESTful)

from flask import request
from flask_restful import Resource
from app.extensions import db
from app.models.purchase_order import PurchaseOrder
from flask_jwt_extended import jwt_required

class PurchaseOrderListResource(Resource):
    @jwt_required()
    def get(self):
        purchase_orders = PurchaseOrder.query.all()
        return [{
            "id": po.id,
            "supplier_id": po.supplier_id,
            "product_id": po.product_id,
            "quantity": po.quantity,
            "status": po.status,
            "created_at": po.created_at
        } for po in purchase_orders], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        try:
            new_po = PurchaseOrder(
                supplier_id=data["supplier_id"],
                product_id=data["product_id"],
                quantity=data["quantity"],
                status=data.get("status", "pending")
            )
            db.session.add(new_po)
            db.session.commit()
            return {"message": "Purchase order created successfully."}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400


# app/routes/customer_routes.py (Flask-RESTful)

from flask import request
from flask_restful import Resource
from app.extensions import db
from app.models.customer import Customer
from flask_jwt_extended import jwt_required

class CustomerListResource(Resource):
    @jwt_required()
    def get(self):
        customers = Customer.query.all()
        return [c.serialize() for c in customers], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        customer = Customer(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            preferences=data.get("preferences"),
            feedback=data.get("feedback")
        )
        db.session.add(customer)
        db.session.commit()
        return customer.serialize(), 201

class CustomerResource(Resource):
    @jwt_required()
    def get(self, id):
        customer = Customer.query.get_or_404(id)
        return customer.serialize(), 200

    @jwt_required()
    def put(self, id):
        customer = Customer.query.get_or_404(id)
        data = request.get_json()
        customer.name = data.get("name", customer.name)
        customer.email = data.get("email", customer.email)
        customer.phone = data.get("phone", customer.phone)
        customer.preferences = data.get("preferences", customer.preferences)
        customer.feedback = data.get("feedback", customer.feedback)
        db.session.commit()
        return customer.serialize(), 200

    @jwt_required()
    def delete(self, id):
        customer = Customer.query.get_or_404(id)
        db.session.delete(customer)
        db.session.commit()
        return {"message": "Customer deleted"}, 200

