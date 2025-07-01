# BizPro Backend

## 🚀 Getting Started

### 1. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize and migrate database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Run the server
```bash
python app.py
```

### 🔐 Notes
- Base URL: `http://127.0.0.1:5000/`
- Use Postman to test: `/auth/register`, `/auth/login`, etc.
- Roles: `admin`, `customer`, `storekeeper`, `supplier`
- Returns JWT token and user details on login.
