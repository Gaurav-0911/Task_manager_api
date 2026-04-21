# 🚀 Task Management API (Flask)

A production-like REST API built using Flask that allows users to manage tasks with secure authentication and full CRUD functionality.

---

## 📌 Features

* 🔐 User Authentication (JWT-based)
* 📝 Task CRUD (Create, Read, Update, Delete)
* 👥 Task Assignment to Users
* 🔍 Pagination & Filtering
* 🔒 Authorization (User-based access control)
* 🧪 Unit Testing using Pytest
* 📮 API Testing using Postman

---

## 🛠️ Tech Stack

* Python (Flask)
* Flask SQLAlchemy (ORM)
* Flask JWT Extended (Authentication)
* Flask Bcrypt (Password Hashing)
* Pytest (Testing)
* Postman (API Testing)

---

## 📁 Project Structure

```
task_manager_api/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   ├── extensions.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_tasks.py
│
├── instance/
│   └── tasks.db
│
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/Gaurav-0911/Task_manager_api
cd task-manager-api
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Server

```
python run.py
```

👉 Server will run on:

```
http://127.0.0.1:5000/
```

---

## 🔑 API Endpoints

### 🔐 Authentication

* `POST /register` → Register a new user
* `POST /login` → Login and receive JWT token

---

### 📋 Tasks

* `POST /tasks` → Create a new task
* `GET /tasks` → Get all tasks (with pagination & filtering)
* `PUT /tasks/{id}` → Update task status
* `DELETE /tasks/{id}` → Delete task

---

## 🔐 Authentication Usage

All protected routes require JWT token:

```
Authorization: Bearer <your_token>
```

---

## 📮 API Testing (Postman)

This project was tested using Postman:

Steps:

1. Register user
2. Login to get token
3. Use token in Authorization header
4. Perform CRUD operations on tasks

---

## 🧪 Running Tests

```
pytest -v
```

✔ Test Coverage Includes:

* User registration
* User login
* Task creation
* Task update
* Task deletion
* Unauthorized access

---

## 📸 Demo (Optional but Recommended)

You can add screenshots of:

* Postman API requests
* Test results (`pytest`)

---

## 🚀 Future Improvements

* Role-based access (Admin/User)
* Task priority & deadlines
* Deployment (Render / Railway)
* Docker support

---

## 👨‍💻 Author

**Kumar Gaurav**

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
