# Django FAQ Project

This is a simple FAQ system built with Django, Django REST Framework, and django-ckeditor. It supports multilingual content, caching with Redis, and automatic translations using googletrans.

## Features

- Stores questions in English and translates them to Hindi and Bengali.
- Uses django-ckeditor for rich text formatting in answers.
- REST API with language selection via query parameters.
- Caches translations with Redis for better performance.
- Basic admin panel for managing FAQs.
- Unit tests using pytest.

## Assumptions
- googletrans is used for translations .
- SQLite is the default database, but you can switch to PostgreSQL or MySQL.
- Redis should be running locally on port 6379.

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



