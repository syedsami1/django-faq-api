# Django FAQ Project

## Introduction
FAQ App is a robust application designed to efficiently manage frequently asked questions (FAQs). Built with Django and Django REST Framework, it provides an intuitive system for storing, retrieving, and managing FAQ content. This application supports multilingual functionality, allowing users to access FAQs in multiple languages. It integrates `django-ckeditor` for rich text formatting, Redis for optimized caching, and `googletrans` for seamless automatic translations. With a well-defined REST API, it ensures smooth communication and easy integration with frontend applications.

## Features

- Stores questions in English and translates them to Hindi and Bengali.
- Uses django-ckeditor for rich text formatting in answers.
- REST API with language selection via query parameters.
- Caches translations with Redis for better performance.
- Basic admin panel for managing FAQs.
- Unit tests using pytest.

## Assumptions
- googletrans is used for translations.
- SQLite is the default database, but you can switch to PostgreSQL or MySQL.
- Redis should be running locally on port 6379.

## Project Structure
```
django-faq-project/
│── config/
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── asgi.py
│   │── wsgi.py
│
│── faq/
│   │── migrations/
│   │── tests/
│   │   │── test_api.py
│   │   │── test_models.py
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── serializers.py
│   │── urls.py
│   │── views.py
│
│── venv/
│── .env
│── .gitignore
│── db.sqlite3
│── manage.py
│── README.md
│── requirements.txt
```

## Setup

### Clone the repository
```bash
git clone https://github.com/syedsami1/django-faq-api.git
cd django-faq-project
```

### Virtual environment
```bash
python -m venv venv
venv\Scripts\activate 

```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Apply migrations
```bash
python manage.py migrate
```

### Create a superuser
```bash
python manage.py createsuperuser
```

### Start Redis 
```bash
redis-server
```

### Run the server
```bash
python manage.py runserver
```

## API Endpoints

- Default (English): `GET /api/faqs/`
- Hindi: `GET /api/faqs/?lang=hi`
- Bengali: `GET /api/faqs/?lang=bn`

Example:
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

## Git & Version Control

### Commit message format
- `feat: Add translation support`
- `fix: Improve caching logic`
- `docs: Update API examples`

### Basic Git workflow
```bash
git add .
git commit -m "feat: Add translation support"
git push origin main
```

## Running tests
```bash
pytest
```
