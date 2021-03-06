# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import emailView, successView

from django.contrib.auth.views import logout_then_login, LoginView

urlpatterns = [
    url(r'^email/', login_required(emailView), name='email'),
    url(r'^success/', successView, name='success'),
]