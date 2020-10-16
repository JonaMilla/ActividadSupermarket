from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .models import Producto
from .forms import ProductoForm

# Create your views here.
def registro(request):
    #GET
    formulario = UserCreationForm()  
    if request.method == 'POST':
        # entro a POST 
        formulario = UserCreationForm(data = request.POST)
        if formulario.is_valid():
            usuarioRegistrado = formulario.save()
            if usuarioRegistrado is not None:
                login(request, usuarioRegistrado)
                return redirect('/perfil/')

    context = {
        'formulario' : formulario
    }
    return render(
        request,
        'usuario/registro.html',
        context
    )
    #POST
def iniciarSesion(request):
    #GET
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']

            usuarioLogeado = authenticate(username = username, password = password)
            if usuarioLogeado is not None:
                login(request, usuarioLogeado)
                return redirect('/perfil/')

    context = {
        'formulario' : formulario
    }
    return render(
        request,
        'usuario/inicio_sesion.html',
        context
    )
    #POST
def salir(request):
    logout(request)
    return redirect('/')

def perfil(request):
    if request.user.is_authenticated:
        return render(
            request,
            'usuario/perfil.html'
        )
    return redirect('/')


# ++++++++CARRITO++++++++
def listarProducto(request):
    productos = Producto.objects.all()
    context = {
        "titulo":"Listar Productos",
        "productos": productos
    }
    return render(
        request,
        'crudProducto/listar_producto.html',
        context
    )

def agregarProducto(request):
    formulario = None   
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto/')
    else:
        formulario = ProductoForm()
    context = {
        "titulo":"Agregar Productos",
        "formulario": formulario
    }
    return render(
        request,
        'crudProducto/agregar_producto.html',
        context
    )

def modificarProducto(request, id_producto):
    productoEncontrado = Producto.objects.get(pk=id_producto)
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=productoEncontrado)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto/')
    else:
        formulario = ProductoForm(instance=productoEncontrado)
    context = {
        "titulo":"Modificar Producto",
        "formulario": formulario
    }
    return render(
        request,
        'crudProducto/modificar_producto.html',
        context
    )

def eliminarProducto(request, id_producto):
    productoEncontrado = Producto.objects.get(pk=id_producto)
    productoEncontrado.delete()
    return redirect('/producto/')