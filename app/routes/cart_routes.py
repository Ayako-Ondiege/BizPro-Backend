from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.cart import Cart, CartItem
from app.models.product import Product
from app.models.user import User
from app.models.order import Order, OrderItem
from app.models.payment import Payment
from datetime import datetime

MINIMUM_STOCK = 5  # Customize this threshold


class CartResource(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        cart = Cart.query.filter_by(customer_id=current_user_id).first()
        if not cart:
            return {"cart": [], "total_price": 0.0}

        cart_data = {
            "id": cart.id,
            "total_quantity": cart.total_quantity(),
            "total_price": cart.total_price(),
            "items": [
                {
                    "product_id": item.product_id,
                    "product_name": item.product.name,
                    "price": item.unit_price,
                    "quantity": item.quantity
                } for item in cart.cart_items
            ]
        }
        return cart_data, 200


class AddToCartResource(Resource):
    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()
            data = request.get_json()

            product_id = data.get("product_id")
            quantity = data.get("quantity")

            if not product_id or not quantity:
                return {"error": "product_id and quantity are required"}, 400

            product = Product.query.get(product_id)
            if not product:
                return {"error": "Product not found"}, 404

            if product.price is None:
                return {"error": f"Product '{product.name}' has no price set."}, 400

            if product.stock < quantity:
                return {"error": f"Not enough stock. Available: {product.stock}"}, 400

            cart = Cart.query.filter_by(customer_id=current_user_id).first()
            if not cart:
                cart = Cart(customer_id=current_user_id)
                db.session.add(cart)
                db.session.commit()

            cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()

            if cart_item:
                cart_item.quantity += quantity
                cart_item.unit_price = product.price  # Update to latest price if needed
            else:
                cart_item = CartItem(
                    cart_id=cart.id,
                    product_id=product_id,
                    quantity=quantity,
                    unit_price=product.price
                )
                db.session.add(cart_item)

            db.session.commit()
            return {"message": "Item added to cart"}, 201

        except Exception as e:
            print("ERROR in AddToCartResource:", e)
            return {"message": "Internal Server Error"}, 500


class CheckoutResource(Resource):
    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()
            cart = Cart.query.filter_by(customer_id=current_user_id).first()

            if not cart or not cart.cart_items:
                return {"error": "Cart is empty"}, 400

            # Check stock before proceeding
            for item in cart.cart_items:
                product = item.product
                if product.stock < item.quantity:
                    return {
                        "error": f"Insufficient stock for '{product.name}' (Available: {product.stock})"
                    }, 400

            # Calculate total
            total_amount = sum(item.unit_price * item.quantity for item in cart.cart_items)

            # Create order
            order = Order(
                customer_id=current_user_id,
                total_amount=total_amount,
                status="Paid"
            )
            db.session.add(order)
            db.session.flush()  # get order.id

            # Create order items
            for item in cart.cart_items:
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    unit_price=item.unit_price
                )
                db.session.add(order_item)

                # Deduct stock
                item.product.stock -= item.quantity

            # Create payment
            payment = Payment(
                order_id=order.id,
                amount=total_amount,
                method="Simulated",
                reference=f"TXN-{order.id}-{int(datetime.utcnow().timestamp())}"
            )
            db.session.add(payment)

            # Notifications for low stock
            notifications = []
            for item in cart.cart_items:
                if item.product.stock <= MINIMUM_STOCK:
                    notifications.append({
                        "product": item.product.name,
                        "stock": item.product.stock,
                        "action": "Notify suppliers to restock"
                    })

            # Clear the cart
            db.session.delete(cart)
            db.session.commit()

            return {
                "message": "Order placed and payment recorded successfully.",
                "order_id": order.id,
                "total_amount": total_amount,
                "payment_reference": payment.reference,
                "notifications": notifications
            }, 200

        except Exception as e:
            print("ERROR in CheckoutResource:", e)
            db.session.rollback()
            return {"message": "Internal Server Error"}, 500


class AddToCartResource(Resource):
    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()
            data = request.get_json()

            product_id = data.get("product_id")
            quantity = data.get("quantity")

            if not product_id or not quantity:
                return {"error": "product_id and quantity are required"}, 400

            product = Product.query.get(product_id)
            if not product:
                return {"error": "Product not found"}, 404

            if product.price is None:
                return {"error": f"Product '{product.name}' has no price set."}, 400

            if product.stock < quantity:
                return {"error": f"Not enough stock. Available: {product.stock}"}, 400

            cart = Cart.query.filter_by(customer_id=current_user_id).first()
            if not cart:
                cart = Cart(customer_id=current_user_id)
                db.session.add(cart)
                db.session.commit()

            cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()

            if cart_item:
                cart_item.quantity += quantity
                cart_item.unit_price = product.price  # Update to latest price if needed
            else:
                cart_item = CartItem(
                    cart_id=cart.id,
                    product_id=product_id,
                    quantity=quantity,
                    unit_price=product.price
                )
                db.session.add(cart_item)

            db.session.commit()
            return {"message": "Item added to cart"}, 201

        except Exception as e:
            print("ERROR in AddToCartResource:", e)
            return {"message": "Internal Server Error"}, 500


class CheckoutResource(Resource):
    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()
            cart = Cart.query.filter_by(customer_id=current_user_id).first()

            if not cart or not cart.cart_items:
                return {"error": "Cart is empty"}, 400

            # Check stock before proceeding
            for item in cart.cart_items:
                product = item.product
                if product.stock < item.quantity:
                    return {
                        "error": f"Insufficient stock for '{product.name}' (Available: {product.stock})"
                    }, 400

            # Calculate total
            total_amount = sum(item.unit_price * item.quantity for item in cart.cart_items)

            # Create order
            order = Order(
                customer_id=current_user_id,
                total_amount=total_amount,
                status="Paid"
            )
            db.session.add(order)
            db.session.flush()  # get order.id

            # Create order items
            for item in cart.cart_items:
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    unit_price=item.unit_price
                )
                db.session.add(order_item)

                # Deduct stock
                item.product.stock -= item.quantity

            # Create payment
            payment = Payment(
                order_id=order.id,
                amount=total_amount,
                method="Simulated",
                reference=f"TXN-{order.id}-{int(datetime.utcnow().timestamp())}"
            )
            db.session.add(payment)

            # Notifications for low stock
            notifications = []
            for item in cart.cart_items:
                if item.product.stock <= MINIMUM_STOCK:
                    notifications.append({
                        "product": item.product.name,
                        "stock": item.product.stock,
                        "action": "Notify suppliers to restock"
                    })

            # Clear the cart
            db.session.delete(cart)
            db.session.commit()

            return {
                "message": "Order placed and payment recorded successfully.",
                "order_id": order.id,
                "total_amount": total_amount,
                "payment_reference": payment.reference,
                "notifications": notifications
            }, 200

        except Exception as e:
            print("ERROR in CheckoutResource:", e)
            db.session.rollback()
            return {"message": "Internal Server Error"}, 500
