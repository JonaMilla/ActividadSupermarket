from django.contrib import admin
from compras.models import Categoria, Producto
# Register your models here.

admin.site.register([Categoria, Producto])
