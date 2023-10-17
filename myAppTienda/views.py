from django.shortcuts import render
from.models import Producto
from django.contrib.auth.decorators import login_required

@login_required
def tienda (request):
    
    productos = Producto.objects.all() #En esta variable almacenamos todoos los objetos ingresados a Producto desde el Admin
    
    return render (request, 'tienda.html', {'productos':productos}) #Se pone coomo 3er parametro al render el listado de los objetos