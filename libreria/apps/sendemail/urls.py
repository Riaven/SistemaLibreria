# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import emailView, successView

urlpatterns = [
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]