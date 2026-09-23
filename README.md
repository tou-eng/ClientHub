# ClientHub - Customer Relationship Management System

A simple Customer Relationship Management (CRM) web application built with **Django**, **PostgreSQL**, and **Bootstrap**. This project focuses on implementing the fundamental **CRUD (Create, Read, Update, Delete)** operations while following Django best practices.

---

## Features

- User Authentication
  - Register
  - Login
  - Logout

- Customer Management
  - Create new customer records
  - View all customer records
  - Update existing records
  - Delete records

- Responsive user interface with Bootstrap

- PostgreSQL database integration

- Django ORM for database operations

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Django | Backend Framework |
| PostgreSQL | Database |
| Bootstrap 5 | Frontend UI |
| HTML5 | Templates |
| CSS3 | Styling |
| Python | Programming Language |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ClientHub.git
cd ClientHub
```

### 2. Create a virtual environment

```bash
python -m venv virt
```

Activate it

Windows

```bash
virt\Scripts\activate
```

Linux/macOS

```bash
source virt/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database.

Example:

```text
Database Name: dCRM
User: postgres
Password: your_password
Port: 5432
```

Update your `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dcrm",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## CRUD Operations

The project demonstrates the four basic database operations:

- ✅ Create customer records
- ✅ Read customer records
- ✅ Update customer information
- ✅ Delete customer records

---


---

## Future Improvements

- Search customers
- Pagination
- User roles and permissions
- Dashboard statistics
- Customer notes
- File uploads
- REST API using Django REST Framework
- Email notifications

---

## Author

**Toufik Menaa**

- GitHub: https://github.com/tou-eng
- LinkedIn: https://www.linkedin.com/in/toufik-menaa-6286602a2/
