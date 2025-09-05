## Setup new project
  - python -m venv .venv 
    - this will create virtual environment.
    
  - pip install django
 
  - django-admin startproject projectname .


## wsgi 
```
Your dev server (python manage.py runserver) doesn’t need this file explicitly because Django internally sets things up for you.
But in production, Nginx/Apache → Gunicorn → wsgi.py → Django.
```

```

Browser (Client)
   ↓
Web Server (Nginx/Apache)
   ↓
WSGI Server (Gunicorn/uWSGI)
   ↓
Django entry point (wsgi.py → application)
   ↓
Django internals (middleware → urls → views → models → templates)
   ↓
Response generated (HTML/JSON/etc.)
   ↓
Back through Gunicorn → Nginx/Apache → Browser
```