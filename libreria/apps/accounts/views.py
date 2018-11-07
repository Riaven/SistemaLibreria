
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.


def user_list(request):
    user = User.objects.all()
    contexto = {'users':user}
    return render(request, 'registration/user_list.html', contexto)

def deshabilitar_user(request, username):
    user = User.objects.get(username=username)
    user.is_active = False
    user.save()
    messages.success(request, 'Profile successfully disabled.')
    return redirect('index')


def mail(request):
    send_mail('Solicitud de despacho',
    'cuaderno alquimia, hojas oficio',
    'librerialmg@gmail.com',
    ['joc.gutierrezl@alumnos.duoc.cl'],
    fail_silently=False)

    return render(request, 'base/send_email.html')

