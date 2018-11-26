from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . views import deshabilitar_user
from django.contrib.auth.views import logout_then_login, LoginView

urlpatterns = [
    url(r'^desabilitar/(?P<id_user>\d+)/$', login_required(deshabilitar_user), name='deshabilitar_user'),
]