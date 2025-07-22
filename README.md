# 📝 Django Blog App

A fully functional Django-based Blog Web Application with role-based access control, JWT authentication, RESTful APIs, blog and comment features, custom signals, management commands, and performance caching.

---

## 🚀 Features

### 👥 Authentication & User Roles
- JWT token authentication using Djoser
- Role-based access:
  - **Admin:** Full control
  - **Staff:** Moderate content
  - **User:** View, comment, create blog posts
- Login/logout with user popup messages
- Display logged-in username in the navbar

### 📚 Blog & Comment System
- Create, Read, Update, Delete (CRUD) for blog posts
- Comment system with author name and time
- Scrollable and styled comment section

### 🔍 Search & Pagination
- Search blogs by title/content
- Paginated blog listing with Bootstrap styling

### 📡 REST API
- Secure API using Django REST Framework
- Blog listing, creation, update, delete with token protection
- Role-based access to endpoints
- User list endpoint (admin only)

### 🛠 Custom Management Commands
- `create_demo_posts <count>`: Generate dummy blogs
- `delete_all_posts`: Delete all blog posts
- Example: `python manage.py create_demo_posts 10`

### 🔔 Signals & Logging
- Logs registration and login actions via custom Django signals

### ⚡ Performance Optimization
- Implemented view-level and low-level caching to boost performance

---

## 🖥️ Tech Stack

- **Backend:** Django, DRF, Djoser
- **Frontend:** HTML, CSS, Bootstrap 5
- **Auth:** JWT + Session Auth
- **Database:** SQLite (easy switch to PostgreSQL)
- **Other:** Django Signals, Caching, Custom Commands

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
    ```bash
        git clone https://github.com/yourusername/django-blog-app.git
        cd django-blog-app

2. **Create virtual environment and install dependencies:**
    ```bash
        python -m venv venv
        source venv\Scripts\activate  
        pip install -r requirements.txt

3. **Apply migrations:**
    ```bash
        python manage.py migrate

4. Create Superuser
    ```bash
    python manage.py createsuperuser

5. Run Server
    ```bash
    python manage.py runserver

---

## 🧪 API Endpoints

| Method | Endpoint           | Description                 | Auth |
| ------ | ------------------ | --------------------------- | ---- |
| POST   | `/api/token/`      | Get access + refresh tokens | ❌    |
| GET    | `/api/blogs/`      | List all blogs              | ✅    |
| POST   | `/api/blogs/`      | Create a blog               | ✅    |
| PUT    | `/api/blogs/<id>/` | Update a blog               | ✅    |
| DELETE | `/api/blogs/<id>/` | Delete a blog               | ✅    |
| GET    | `/api/users/`      | List all users (admin only) | ✅    |

---

## 💡 Highlights
🎯 Role-Based Access Control

🔐 JWT Authentication with Djoser

🧠 Custom Django Signals

⚙️ Management Commands

🚀 DRF API with Permissions

⚡ View-level Caching