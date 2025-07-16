from app.extensions import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(50), unique=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    category = db.Column(db.String(100))
    min_order_quantity = db.Column(db.Integer, nullable=False, default=5)
    description = db.Column(db.String(255))  # ✅ To support seed data descriptions

    # Optional: relationships (e.g., with CartItems or OrderItems)
    # cart_items = db.relationship("CartItem", back_populates="product", lazy=True)

    def __repr__(self):
        return f"<Product {self.name} - ${self.price}>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "sku": self.sku,
            "price": self.price,
            "stock": self.stock,
            "category": self.category,
            "min_order_quantity": self.min_order_quantity,
            "description": self.description
        }

