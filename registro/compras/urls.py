from django.urls import path
from .views import index, crear_producto

urlpatterns = [
    path('', index, name='carrito'),
    path('crear/producto', crear_producto, name='crear_producto'),
]
