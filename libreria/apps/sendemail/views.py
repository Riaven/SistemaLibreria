# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['panchaguerrerodiaz@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('sendemail:success')
    return render(request, "registration/email.html", {'form': form})

def successView(request):
    return HttpResponse('Tu solicitud de despacho ha sido enviada exitosamente')