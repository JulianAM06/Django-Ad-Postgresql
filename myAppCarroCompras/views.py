from django.shortcuts import render
from django.shortcuts import redirect
from myAppCarroCompras.carro import Carrito
from myAppTienda.models import Producto


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect ('/tienda')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect ('/tienda')
    
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect ('/tienda')

def limpiar_carrito(request):
    carrito = Carrito(request) 
    carrito.limpiar()  
    return redirect ('/tienda') 

