from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.product import Product
from app.models.user import User

# Product Routes
class ProductListResource(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        allowed_roles = ["admin", "storekeeper", "customer"]
        if not user or user.role.lower() not in allowed_roles:
            return {"error": "Unauthorized access"}, 403

        products = Product.query.all()
        return [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "stock": p.stock,
                "description": p.description
            } for p in products
        ], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        try:
            new_product = Product(
                name=data["name"],
                price=data["price"],
                stock=data.get("stock", 0),
                description=data.get("description")
            )
            db.session.add(new_product)
            db.session.commit()
            return {"message": "Product created successfully."}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400

class ProductResource(Resource):
    @jwt_required()
    def get(self, id):
        product = Product.query.get_or_404(id)
        return {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "description": product.description
        }, 200

    @jwt_required()
    def put(self, id):
        product = Product.query.get_or_404(id)
        data = request.get_json()
        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.stock = data.get("stock", product.stock)
        product.description = data.get("description", product.description)
        db.session.commit()
        return {"message": "Product updated successfully."}, 200

    @jwt_required()
    def delete(self, id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}, 200
