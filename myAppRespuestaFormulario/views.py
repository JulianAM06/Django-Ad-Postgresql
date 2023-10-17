from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from myAppRespuestaFormulario.forms import FormularioContacto

def contact (request):
    
    if request.method=='POST':
        
        subject = request.POST['name']
        
        subject = request.POST['last']
        
        subject = request.POST['number']
        
        message = request.POST['name'] + ' ' + request.POST['last'] + ' ' + request.POST['number'] + ' ' + request.POST['message'] + ' ' + request.POST['email']
        
        email_from = settings.EMAIL_HOST_USER
        
        recipient_list = ['michi.adelle10@gmail.com']
        
        send_mail(subject, message, email_from, recipient_list)
        
        return render (request, 'gracias.html')
    
    return render (request, 'contact.html')


#Esta configuracion es para la respuesta del Formulario, se inserta en el Proyecto Ppal,settings.py

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'michi.adelle10@gmail.com'
#EMAIL_HOST_PASSWORD = 'qcym pyyg klgb ljja'