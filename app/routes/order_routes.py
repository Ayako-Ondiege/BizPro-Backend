# app/routes/order_routes.py (Flask-RESTful)

from flask import request
from flask_restful import Resource
from app.extensions import db
from app.models.order import Order
from flask_jwt_extended import jwt_required

class OrderListResource(Resource):
    @jwt_required()
    def get(self):
        orders = Order.query.all()
        return [
            {
                "id": o.id,
                "customer_id": o.customer_id,
                "product_id": o.product_id,
                "quantity": o.quantity,
                "total_price": o.total_price,
                "created_at": o.created_at.isoformat()
            } for o in orders
        ], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        try:
            new_order = Order(
                customer_id=data["customer_id"],
                product_id=data["product_id"],
                quantity=data["quantity"],
                total_price=data["total_price"]
            )
            db.session.add(new_order)
            db.session.commit()
            return {"message": "Order created successfully."}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400

class OrderResource(Resource):
    @jwt_required()
    def get(self, id):
        order = Order.query.get_or_404(id)
        return {
            "id": order.id,
            "customer_id": order.customer_id,
            "product_id": order.product_id,
            "quantity": order.quantity,
            "total_price": order.total_price,
            "created_at": order.created_at.isoformat()
        }, 200

    @jwt_required()
    def put(self, id):
        order = Order.query.get_or_404(id)
        data = request.get_json()
        order.customer_id = data.get("customer_id", order.customer_id)
        order.product_id = data.get("product_id", order.product_id)
        order.quantity = data.get("quantity", order.quantity)
        order.total_price = data.get("total_price", order.total_price)
        db.session.commit()
        return {"message": "Order updated successfully."}, 200

    @jwt_required()
    def delete(self, id):
        order = Order.query.get_or_404(id)
        db.session.delete(order)
        db.session.commit()
        return {"message": "Order deleted."}, 200
