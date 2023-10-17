from django.db import models

class CategoriaProducto(models.Model):
    
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) #auto_now_add se usa para que tome la fecha actualizada
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:  #Esta clase se usa para que salgan los nombres en singular y/o plural
        
        verbose_name = 'CategoriaProducto'
        verbose_name_plural = 'CategoriasProductos'
        
    
    def __str__(self):
        return self.nombre
            
        
class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE) #ForeignKey sirve para relacionar la primera tabla con este campo, on_delete sirve para eliminar todos los productos que existan en una categoria si se elimina dicha categoria
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True) # Se debe tener instalado pillow para que funcionen las imagenes, upload_to, para que carguen en la pagina tienda, null y blank son para que el campo funcione sin necesidad de tener una imagen
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True) # Default = True se usa por si no se indica la disponibilidad, siempre sea disponible
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta: 
         
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
         
         
# Luego se ejecuta python manage.py makemigrations y luego python manage.py migrate