# app/routes/api.py

from flask_restful import Api

# Import your resource classes
from app.routes.product_routes import ProductListResource, ProductResource
from app.routes.supplier_routes import SupplierListResource
from app.routes.order_routes import OrderListResource
from app.routes.customer_routes import CustomerListResource, CustomerResource

def register_api_routes(app):
    api = Api(app)

    # Products
    api.add_resource(ProductListResource, "/products", endpoint="products")
    api.add_resource(ProductResource, "/products/<int:id>", endpoint="product")

    # Suppliers
    api.add_resource(SupplierListResource, "/suppliers", endpoint="suppliers")

    # Orders
    api.add_resource(OrderListResource, "/orders", endpoint="orders")

    # Customers
    api.add_resource(CustomerListResource, "/customers", endpoint="customers")
    api.add_resource(CustomerResource, "/customers/<int:id>", endpoint="customer")

    return api
