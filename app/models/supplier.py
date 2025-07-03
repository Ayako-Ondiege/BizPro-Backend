from app.extensions import db
from datetime import datetime

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    purchases = db.relationship("PurchaseOrder", backref="supplier", lazy=True)
