from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Example extra fields
    phone = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=20, default="user")
