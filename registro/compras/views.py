from django.shortcuts import render, redirect
from compras.forms import FormularioProducto
from django.contrib import messages
from compras.models import Producto
from django.core.paginator import Paginator
#importando decoradores
from django.contrib.auth.decorators import login_required


@login_required(login_url='/cuenta/login')
def index(request):
    listado_productos = Producto.objects.all()
    paginator = Paginator(listado_productos, 3)
    pagina = request.GET.get("page") or 1
    listar_productos = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listar_productos.paginator.num_pages + 1)
    return render(
        request,
        'carrito.html',
        {
            'listar_productos': listar_productos,
            'paginas': paginas,
            'pagina_actual': pagina_actual
        }
    )


@login_required(login_url='/cuenta/login')
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


@login_required(login_url='/cuenta/login')
def eliminarProducto(request, producto_id):
    #Eliminar el producto por su id
    try:
        producto = Producto.objects.get(pk=producto_id)
    # Cuando no exista el producto le enviamos un mensaje y redireccionamos a la página principal
    except Producto.DoesNotExist:
        messages.error(request, "El producto que desea eliminar no se encuentra en tu lista")
        return redirect("carrito")
    # comprobamos si soy el autor del producto
    if producto.autor != request.user:
        messages.error(request, "No eres el autor de este producto")
        return redirect("carrito")
    #si soy el autor pues elimino el producto y redireccionamos a la página principal
    producto.delete()
    messages.success(request, F"El producto { producto.nombre_producto } se ha eliminado de la lista")
    return redirect("carrito")
