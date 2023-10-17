"""
URL configuration for ADIDAS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myAppPrincipal.views import inicio
from myAppTienda.views import tienda
from myAppRespuestaFormulario.views import contact
from myAppCarroCompras.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
from myAppAutenticacion.views import cerrar_sesion, iniciar, register
from myAppPedidos.views import procesar_pedido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('tienda/',tienda),
     path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="Cls"),
    path('contact/', contact),
    path('cerrar_cesion/', cerrar_sesion, name='cerrar_cesion'),
    path('login/', iniciar, name='login'),
    path('accounts/', include ('django.contrib.auth.urls')),
    path('pedidos/',procesar_pedido, name='procesar_pedido'),
    path('registro/', register, name= 'register'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)