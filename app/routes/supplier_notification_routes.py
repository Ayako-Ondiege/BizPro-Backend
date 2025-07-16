from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.supplier_notification import SupplierNotification
from app.utils.auth_helpers import role_required

class SupplierNotificationList(Resource):
    @jwt_required()
    @role_required("admin", "storekeeper", "supplier")  # only these roles can view
    def get(self):
        notifications = SupplierNotification.query.order_by(SupplierNotification.created_at.desc()).all()
        return [{
            "id": n.id,
            "product_id": n.product_id,
            "supplier_id": n.supplier_id,
            "message": n.message,
            "created_at": n.created_at.isoformat(),
            "is_read": n.is_read
        } for n in notifications], 200


class SupplierNotificationDetail(Resource):
    @jwt_required()
    @role_required("admin", "supplier")  # limit who can fetch specific
    def get(self, id):
        notification = SupplierNotification.query.get_or_404(id)
        return {
            "id": notification.id,
            "product_id": notification.product_id,
            "supplier_id": notification.supplier_id,
            "message": notification.message,
            "created_at": notification.created_at.isoformat(),
            "is_read": notification.is_read
        }, 200


class SupplierNotificationMarkRead(Resource):
    @jwt_required()
    @role_required("supplier")  # only suppliers can mark read
    def put(self, id):
        notification = SupplierNotification.query.get_or_404(id)
        notification.is_read = True
        db.session.commit()
        return {"message": "Notification marked as read."}, 200


