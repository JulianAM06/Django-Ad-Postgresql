from django.shortcuts import render, redirect
from myAppPedidos.models import Pedido, LineaPedido
from myAppCarroCompras.carro import Carrito
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

def procesar_pedido(request):
    
    pedido = Pedido.objects.create(user=request.user)
    carro = Carrito(request)
    lineas_pedido = list()
    
    for key, value in carro.carrito.items():
        
        lineas_pedido.append(LineaPedido(
            
            producto_id = key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
            
        ))
        
    LineaPedido.objects.bulk_create(lineas_pedido) 
    
    enviar_mail(
        
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email,
    
    )   
    
    messages.success(request, 'El pedido se ha cargado correctamente')
    
    return redirect ('/tienda/')

def enviar_mail(**kwargs):
    
    asunto = 'Gracias por tu Pedido'
    mensaje = render_to_string('pedidos.html',{
        
        'pedido': kwargs.get('pedido'),
        'lineas_pedido':kwargs.get('lineas_pedido'),
        'nombreusuario':kwargs.get('nombreusuario')
         
    })
    
    mensaje_texto = strip_tags(mensaje)
    from_email = 'michi.adelle10@gmail.com'
    to=kwargs.get('emailusuario')
    
    
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
        
        
        
        
    
    