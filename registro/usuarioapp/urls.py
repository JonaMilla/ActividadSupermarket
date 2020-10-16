from django.urls import path
from .views import registro, iniciarSesion, salir, perfil, listarProducto, agregarProducto, modificarProducto, eliminarProducto

urlpatterns = [
    path('', iniciarSesion, name='iniciarSesion'),
    path('registrar/', registro, name='registro'),
    path('salir/', salir, name='salir'),
    path('perfil/', perfil, name='perfil'),
    path('',listarProducto, name='listar_producto'),
    path('agregar/',agregarProducto, name='agregar_producto'),
    path('editar/<int:id_producto>', modificarProducto, name='modificar_producto'),
    path('eliminar/<int:id_producto>', eliminarProducto, name='eliminar_producto')
    
]