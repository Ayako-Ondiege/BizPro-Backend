from app.extensions import db
from app.models.user import User
from app.models.supplier import Supplier
from app import create_app
from faker import Faker
import random

app = create_app()
fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Admin and Storekeeper
    admin_user = User(username="admin", email="admin@example.com", role="admin")
    admin_user.set_password("admin123")

    storekeeper = User(username="storekeeper", email="store@example.com", role="storekeeper")
    storekeeper.set_password("store123")

    users = [admin_user, storekeeper]

    # Seed 15 Customers
    for _ in range(15):
        username = fake.user_name()
        email = fake.unique.email()
        customer = User(username=username, email=email, role="customer")
        customer.set_password("customer123")
        users.append(customer)

    db.session.add_all(users)

    # Seed 50 Suppliers
    suppliers = []
    for _ in range(50):
        name = fake.company()
        email = fake.unique.company_email()
        phone = fake.unique.phone_number()
        supplier = Supplier(name=name, email=email, phone=phone)
        suppliers.append(supplier)

    db.session.add_all(suppliers)

    db.session.commit()
    print("✅ Users and suppliers seeded successfully.")