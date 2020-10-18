from django.shortcuts import render, redirect
from compras.forms import FormularioProducto
from django.contrib import messages
from compras.models import Producto
# Create your views here.

def index(request):
    listar_productos = Producto.objects.all()
    return render(
        request,
        'carrito.html',
        {'listar_productos': listar_productos}
    )

def crear_producto(request):
    if request.method == 'POST':
        form = FormularioProducto(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.autor_id = request.user.id
            product.save()
            nombrePro = form.cleaned_data.get("nombre_producto")
            messages.success(request, F"El producto {nombrePro} se ha creado con éxito")
            return redirect("carrito")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    form = FormularioProducto()
    return render(
        request,
        'crear_producto.html',
        {'form': form}
    )
