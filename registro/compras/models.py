from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre
    
    class Meta:
        #cambiar el nombre a la tabla en la base de datos
        db_table = 'Categoria' 
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-id']

class Producto(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100, unique=True, null=False, verbose_name='Nombre del producto')
    precio = models.PositiveIntegerField(null=True, blank=True, verbose_name='Precio del producto')
    descripcion = models.TextField(null=True,verbose_name='Descripción del producto')
    imagen = models.ImageField(upload_to='media/%d/%m/%Y', null=True, blank=True, verbose_name='Imagen del producto')
    fecha_creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    fecha_modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')

    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        #cambiar el nombre a la tabla en la base de datos
        db_table = 'producto' 
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']