# BizPro Backend

Flask-based REST API backend for **BizPro** – a role-based construction management platform supporting Admins, Customers, Storekeepers, and Suppliers.

This backend includes:
- 🔐 JWT Authentication
- 🧱 Modular architecture (Blueprints, Models, Schemas)
- 🧪 Admin seeding and role-based route protection
- 🔄 Flask-Migrate for schema versioning
- 🌱 Environment configuration with `.env` and `.env.example`

---

## 🚀 Tech Stack

- **Python 3.12**
- **Flask**
- **SQLAlchemy + PostgreSQL / SQLite**
- **Flask-Migrate**
- **Flask-JWT-Extended**
- **Marshmallow**
- **Flask-CORS**
- **dotenv**

---

## 📁 Folder Structure

backend/
├── app/
│ ├── init.py
│ ├── extensions.py
│ ├── models/
│ │ └── user.py
│ ├── routes/
│ │ ├── auth_routes.py
│ │ └── main_routes.py
│ ├── schemas/
│ │ └── user_schema.py
│ ├── controllers/ # (for future logic)
│ └── utils/
│ └── security.py
├── migrations/
├── seed.py # Seeds default admin user
├── config.py
├── app.py
├── .env.example
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/BizPro-Backend.git
cd BizPro-Backend
Create virtual environment and activate

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create .env file

bash
Copy
Edit
cp .env.example .env
Update values in .env for your environment.

🛠️ Migrate & Seed Database
bash
Copy
Edit
flask db upgrade
python seed.py
🏁 Run the App
bash
Copy
Edit
flask run
Base URL: http://localhost:5000

🔐 Auth Routes
Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	Login and receive a token
GET	/auth/me	Get current user info
GET	/admin-only	Protected: Admins only

Use JWT in headers: Authorization: Bearer <token>

🧪 Default Admin Credentials
json
Copy
Edit
{
  "username": "admin",
  "email": "admin@bizpro.com",
  "password": "admin123"
}