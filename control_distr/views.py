from django.shortcuts import render, redirect
from django.urls import reverse
from control_distr.models import productos, clientes
from .forms import ProductoForm, ClienteForm


def saludar_con_html(request):
    contexto = {
        'saludo': 'Bienvenido a distribuidora LG!',
    }
    return render(request, 'control_distr/inicio.html', contexto)

def listar_productos(request):
    contexto = {
        "productos": productos.objects.all(),
    }
    return render(request, 'control_distr/lista_productos.html', contexto)

def listar_clientes(request):
    contexto = {
        "clientes": clientes.objects.all(),
    }
    return render(request, 'control_distr/lista_clientes.html', contexto)


def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            numero_cliente = form.cleaned_data["numero_cliente"]
            calle = form.cleaned_data["calle"]
            calle_altura = form.cleaned_data["calle_altura"]
            telefono = form.cleaned_data["telefono"]
            cliente = clientes(nombre=nombre, apellido=apellido, numero_cliente=numero_cliente, calle=calle, calle_altura=calle_altura, telefono=telefono)
            cliente.save()
            url_exitosa = reverse('lista_clientes')
            return redirect(url_exitosa)
    else:
        form = ClienteForm()
    
    contexto = {
        'form': form
    }
    return render(request, 'control_distr/formulario_cliente.html', contexto)

def buscar_clientes(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        resultados = clientes.objects.filter(numero_cliente__contains=busqueda)
        contexto = {
            "clientes": resultados,
        }
        http_response = render(
            request=request,
            template_name='control_distr/lista_clientes.html',
            context=contexto,
        )
        return http_response
    
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            precio = form.cleaned_data["precio"]
            resultado = productos(nombre=nombre, precio=precio)
            resultado.save()
            url_exitosa = reverse('lista_productos')
            return redirect(url_exitosa)
    else:
        form = ProductoForm()
    
    contexto = {
        'form': form
    }
    return render(request, 'control_distr/formulario_producto.html', contexto)


def buscar_producto(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        resultados = productos.objects.filter(nombre__contains=busqueda)
        contexto = {
            "productos": resultados,
        }
        return render(request, 'control_distr/lista_productos.html', contexto)

