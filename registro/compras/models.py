from django.db import models
from django.contrib.auth.models import User
#al eliminar un producto támbien se borre el archivo(imagen) vinculado,
#para esto hay que importar os para acceder al sistema de archivos
import os

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

    """Está función se encuentra disponible en el modelo Producto
    y ahora la sobreescribimos, para mirar si existe este archivo(imagen)
    y si existe el archivo(imagen) al momento de eliminar el producto entonces 
    eliminamos el archivo juntamente con el producto"""
    def delete(self, *args, **Kwargs):
        if os.path.isfile(self.imagen.path):
            #si el archivo existe se elimina
            os.remove(self.imagen.path)
            # el super se ocupa para llamar al constructor y en este caso pasar el producto
        super(Producto, self).delete(*args, **Kwargs)

    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        #cambiar el nombre a la tabla en la base de datos
        db_table = 'producto' 
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']