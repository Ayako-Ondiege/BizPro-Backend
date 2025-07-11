from app.extensions import db
from app.models.user import User
from app.models.supplier import Supplier

# Create the application context if not already set
from app import create_app
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create users
    admin_user = User(username="admin", email="admin@example.com", role="admin")
    admin_user.set_password("admin123")

    storekeeper = User(username="storekeeper", email="store@example.com", role="storekeeper")
    storekeeper.set_password("store123")

    db.session.add_all([admin_user, storekeeper])

    # Create suppliers
    supplier1 = Supplier(name="ABC Supplies", email="abc@example.com", phone="0712345678")
    supplier2 = Supplier(name="XYZ Distributors", email="xyz@example.com", phone="0723456789")

    db.session.add_all([supplier1, supplier2])

    db.session.commit()
    print("✅ Database seeded successfully.")

