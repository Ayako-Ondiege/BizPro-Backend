# app/routes/supplier_routes.py

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.utils.security import role_required
from app.extensions import db
from app.models.supplier import Supplier

class SupplierListResource(Resource):
    @jwt_required()
    @role_required(["admin", "storekeeper"])
    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Missing JSON payload"}, 400

        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")

        if not all([name, email, phone]):
            return {"error": "name, email, and phone are required"}, 400

        supplier = Supplier(name=name, email=email, phone=phone)
        db.session.add(supplier)
        db.session.commit()

        return {
            "message": "Supplier created successfully",
            "supplier": {
                "id": supplier.id,
                "name": supplier.name,
                "email": supplier.email,
                "phone": supplier.phone
            }
        }, 201

    @jwt_required()
    def get(self):
        suppliers = Supplier.query.all()
        return [
            {
                "id": s.id,
                "name": s.name,
                "email": s.email,
                "phone": s.phone
            } for s in suppliers
        ], 200
