from django.urls import path
from .views import index, crear_producto, eliminarProducto

urlpatterns = [
    path('', index, name='carrito'),
    path('crear/producto', crear_producto, name='crear_producto'),
    path('eliminar/producto/<int:producto_id>', eliminarProducto, name='eliminarProducto'),
]
