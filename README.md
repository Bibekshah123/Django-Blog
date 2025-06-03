# 📝 Django Blog App

A full-featured blog web application built with Django and Django REST Framework. It supports JWT authentication, user roles (admin, staff, and regular users), full CRUD operations for posts and comments, custom signals, caching, custom management commands, and a responsive UI.

---

## 🚀 Features

### 🔐 Authentication
- JWT token-based authentication using Djoser.
- Role-based access control: Admin, Staff, and Regular Users.
- User registration and login system with popup messages.
- Logged-in user name displayed in the navbar.

### 📰 Blog & Comment System
- Create, Read, Update, Delete (CRUD) functionality for blog posts and comments.
- Each comment displays the author and timestamp.
- Scrollable and styled comment section for better UX.

### 🔎 Search & Pagination
- Search blogs by title or content.
- Paginated blog list with Bootstrap-styled navigation.

### 📂 API Endpoints (Django REST Framework)
- JWT-protected APIs for listing, creating, updating, and deleting blog posts.
- User listing API with secure access.
- Custom permissions based on roles.
- API views use `APIView` and serializers for structured responses.

### 📡 Signals & Logs
- Signals log user registration and login actions.
- Useful for auditing and monitoring user behavior.

### 🛠 Custom Django Commands
- Custom `BaseCommand` implementations to:
  - Create demo posts.
  - Bulk delete posts.
  - Log actions or export data (example use cases).
  
### 💾 Caching
- Caching implemented for views using Django’s low-level and per-view caching.
- Boosts performance by avoiding redundant database queries.

### 💻 Responsive UI
- Bootstrap 5-based clean and mobile-friendly design.
- Fixed-top navbar and sticky footer.
- Social media links in the footer.

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework, Djoser, JWT
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default), PostgreSQL-compatible
- **Auth:** JWT, Session Authentication
- **Caching:** Django’s local-memory caching
- **Others:** Django Signals, Custom Management Commands

---


## 🔧 Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/django-blog-app.git
    cd django-blog-app
2. **Create a virtual environement**
   ```bash
   python -m venv venv
   venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Apply migration and run the server**
   ```bash
   python manage.py migrate
   python manage.py runserver
5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
6. Visit http://127.0.0.1:8000/ in your browser.

 ---


🛡 Permissions & Roles
Role	Access Level
Admin	Full access to all features
Staff	Can manage posts and comments
Regular	Can view, comment, and create posts


---


📬 API Endpoints
POST /api/token/ – Get JWT token

GET /api/blogs/ – List blogs (JWT required)

POST /api/blogs/ – Create a blog (role-protected)

PUT /api/blogs/<id>/ – Update a blog

DELETE /api/blogs/<id>/ – Delete a blog

GET /api/users/ – List all users (admin only)

---


🙌 Contribution
Pull requests and contributions are welcome. For major changes, open an issue first to discuss your ideas.





