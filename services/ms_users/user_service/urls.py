"""
URL configuration for user_service project.

"""
from django.contrib import admin
from django.urls import path


from django.urls import re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^users/', include('users.urls')), #  http://127.0.0.1:8000/users/1
]

