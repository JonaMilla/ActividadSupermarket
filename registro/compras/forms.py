from django import forms
from django.forms import fields
from .models import Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('categoria', 'nombre_producto', 'precio', 'descripcion', 'imagen')