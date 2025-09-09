
Step 1: Create auth_service
    django-admin startproject auth_service
    cd auth_service
    python manage.py startapp accounts

Step 2: Install JWT library
    pip install djangorestframework djangorestframework-simplejwt

Step 3: Update auth_service/settings.py
    INSTALLED_APPS = [
        ...
        "rest_framework",
        "rest_framework_simplejwt",
        "accounts",
    ]

    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ),
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework.renderers.JSONRenderer",
        ),
    }

Step 4: Create a Custom User Model (accounts/models.py)
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class User(AbstractUser):
        # Example extra fields
        phone = models.CharField(max_length=15, null=True, blank=True)
        role = models.CharField(max_length=20, default="user")


    Update settings.py:
    AUTH_USER_MODEL = "accounts.User"

Step 5: Auth Endpoints (accounts/views.py)
Step 6: Serializers (accounts/serializers.py)
Step 7: URLs (auth_service/urls.py)

Step 8: Usage
    Register a User
    ---------------
    POST http://localhost:8000/auth/register/
    Content-Type: application/json

    {
      "username": "alice",
      "email": "alice@example.com",
      "password": "alice123",
      "phone": "9999999999",
      "role": "user"
    }

    Login (Get JWT Token)
    ---------------------
    POST http://localhost:8000/auth/login/
    Content-Type: application/json

    {
      "username": "alice",
      "password": "alice123"
    }

    Response:
    ---------
    {
      "refresh": "xxxx.yyyy.zzzz",
      "access": "aaaa.bbbb.cccc"
    }

    Refresh Token
    -------------
    POST http://localhost:8000/auth/refresh/
    {
      "refresh": "xxxx.yyyy.zzzz"
    }


=======================================================
    Error: ValueError: Dependency on app with no migrations: accounts

    1. Delete old DB & migrations
    rm db.sqlite3
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

    2. Recreate migrations
    python manage.py makemigrations accounts
    python manage.py migrate

    If You Already Migrated Before
        If you already ran migrations and don’t want to drop DB:

        Ensure settings.py has:

        AUTH_USER_MODEL = "accounts.User"


        Then fake the migration for the custom user:

        python manage.py makemigrations accounts
        python manage.py migrate --fake-initial


        This tells Django: “Yes, I know the table already exists, just mark it as applied.”



