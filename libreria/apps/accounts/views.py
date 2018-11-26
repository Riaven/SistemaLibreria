
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.


def user_list(request):
    user = User.objects.all()
    contexto = {'users':user}
    return render(request, 'registration/user_list.html', contexto)

def deshabilitar_user(request, id_user):
    # Se comprueba que el usuario que ingresará a esta función sea un Súper usuario
    if request.user.is_superuser:    
        # Se obtiene a todos los usuarios y se filtra por el id solicitado y se pasa a una variable el id del user solicitado para trabajar
        # con ese id más adelante
        user = User.objects.get(id=id_user)
        if request.method == 'POST':
            # Se verifica que el usuario esta habilitado para deshabilitarlo
            if user.is_active:
                user.is_active = False
                user.save()
               
            else:
                # De lo contrario, si el user esta deshabilitado se habilita
                user.is_active = True
                user.save()
                
            return redirect('user_listar')
        return render(request,'registration/user_disable.html', {'user':user})
    else:
        return HttpResponseNotFound('<h1>Página no encontrada o no tienes los suficientes permisos para entrar a ella :(</h1>')


def mail(request):
    send_mail('Solicitud de despacho',
    'cuaderno alquimia, hojas oficio',
    'librerialmg@gmail.com',
    ['joc.gutierrezl@alumnos.duoc.cl'],
    fail_silently=False)

    return render(request, 'base/send_email.html')

