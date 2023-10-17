from django.contrib import admin
from .models import LineaPedido, Pedido


admin.site.register([Pedido, LineaPedido])

