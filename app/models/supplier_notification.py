from app.extensions import db
from app.models.product import Product
from app.models.supplier import Supplier
from datetime import datetime

class SupplierNotification(db.Model):
    __tablename__ = 'supplier_notifications'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=True)  # Optional
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)


def notify_suppliers(notifications):
    for note in notifications:
        product = note.get("product")
        stock = note.get("stock")

        product_obj = Product.query.filter_by(name=product).first()
        if not product_obj:
            continue

        suppliers = Supplier.query.all()  # Simplified: all suppliers notified

        for supplier in suppliers:
            message = f"Stock Alert: '{product}' stock is low ({stock} left). Please restock immediately."
            notification = SupplierNotification(
                product_id=product_obj.id,
                supplier_id=supplier.id,
                message=message
            )
            db.session.add(notification)

    db.session.commit()
    return True
