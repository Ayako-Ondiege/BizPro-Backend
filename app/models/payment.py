from app.extensions import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    method = db.Column(db.String(50), nullable=False, default="Simulated")
    reference = db.Column(db.String(100), unique=True, nullable=False)
    paid_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Optional relationship back to order
    order = db.relationship("Order", backref="payment")
