# seed.py

from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

with app.app_context():
    if not User.query.filter_by(username="admin").first():
        admin = User(
            username="admin",
            email="admin@bizpro.com",
            role="admin"
        )
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("✅ Default admin user created.")
    else:
        print("⚠️ Admin already exists.")
