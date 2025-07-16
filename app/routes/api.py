# app/routes/api.py

from flask_restful import Api

# Product, Supplier, Order, Customer, Cart Resources
from app.routes.product_routes import ProductListResource, ProductResource
from app.routes.supplier_routes import SupplierListResource, SupplierResource
from app.routes.order_routes import OrderListResource
from app.routes.customer_routes import CustomerListResource, CustomerResource
from app.routes.cart_routes import CartResource, AddToCartResource, CheckoutResource

# ✅ Import Supplier Notification Resources
from app.routes.supplier_notification_routes import (
    SupplierNotificationList,
    SupplierNotificationDetail,
    SupplierNotificationMarkRead
)

def register_api_routes(app):
    api = Api(app)

    # Products
    api.add_resource(ProductListResource, "/products", endpoint="products")
    api.add_resource(ProductResource, "/products/<int:id>", endpoint="product")

    # Suppliers
    api.add_resource(SupplierListResource, "/suppliers", endpoint="suppliers")
    api.add_resource(SupplierResource, "/suppliers/<int:id>", endpoint="supplier")

    # Orders
    api.add_resource(OrderListResource, "/orders", endpoint="orders")

    # Customers
    api.add_resource(CustomerListResource, "/customers", endpoint="customers")
    api.add_resource(CustomerResource, "/customers/<int:id>", endpoint="customer")

    # ✅ Cart
    api.add_resource(CartResource, "/cart", endpoint="cart")
    api.add_resource(AddToCartResource, "/cart/add", endpoint="cart_add")
    api.add_resource(CheckoutResource, "/cart/checkout", endpoint="cart_checkout")

    # ✅ Supplier Notifications
    api.add_resource(SupplierNotificationList, "/notifications/suppliers", endpoint="supplier_notifications")
    api.add_resource(SupplierNotificationDetail, "/notifications/suppliers/<int:id>", endpoint="supplier_notification")
    api.add_resource(SupplierNotificationMarkRead, "/notifications/suppliers/<int:id>/mark-read", endpoint="mark_supplier_notification_read")

    return api

