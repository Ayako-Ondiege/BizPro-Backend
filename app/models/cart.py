from app.extensions import db
from datetime import datetime

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    cart_items = db.relationship("CartItem", back_populates="cart", cascade="all, delete-orphan", lazy=True)

    def total_quantity(self):
        return sum(item.quantity for item in self.cart_items)

    def total_price(self):
        return sum(item.quantity * item.unit_price for item in self.cart_items)


class CartItem(db.Model):
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

    # Relationships
    cart = db.relationship("Cart", back_populates="cart_items", lazy=True)
    product = db.relationship("Product", lazy=True)
