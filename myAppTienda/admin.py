from django.contrib import admin
from.models import CategoriaProducto, Producto


# Estas clases nos permiten enlazar los modelos creados en el panel del Admin, en este caso para agregar Categorias y Productos


class CategoriaProductoAdmin(admin.ModelAdmin): 
    readonly_fields = ('created', 'updated')


admin.site.register(CategoriaProducto, CategoriaProductoAdmin)


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Producto, ProductoAdmin)
    
    