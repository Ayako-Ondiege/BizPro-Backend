# app/routes/order_routes.py (Flask-RESTful)

# app/routes/order_routes.py

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.order import Order
from app.extensions import db

class OrderListResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        orders = Order.query.filter_by(customer_id=user_id).order_by(Order.created_at.desc()).all()

        order_list = []
        for order in orders:
            order_list.append({
                "id": order.id,
                "status": order.status,
                "total_amount": order.total_amount,
                "created_at": order.created_at.isoformat(),
                "items": [
                    {
                        "product_id": item.product_id,
                        "quantity": item.quantity,
                        "unit_price": item.unit_price
                    } for item in order.items
                ]
            })

        return {"orders": order_list}, 200


class OrderResource(Resource):
    @jwt_required()
    def get(self, id):
        order = Order.query.get_or_404(id)
        return {
            "id": order.id,
            "customer_id": order.customer_id,
            "status": order.status,
            "total_amount": order.total_amount,
            "created_at": order.created_at.isoformat(),
            "items": [
                {
                    "product_id": item.product_id,
                    "quantity": item.quantity,
                    "unit_price": item.unit_price
                } for item in order.items
            ]
        }, 200

    @jwt_required()
    def delete(self, id):
        order = Order.query.get_or_404(id)
        db.session.delete(order)
        db.session.commit()
        return {"message": "Order deleted."}, 200
