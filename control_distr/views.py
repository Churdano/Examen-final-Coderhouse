from django.shortcuts import render, redirect
from django.urls import reverse
from control_distr.models import productos, clientes

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
        data = request.POST
        nombre = data.get("nombre")
        apellido = data.get("apellido")
        numero_cliente = data.get("numero_cliente")
        calle = data.get("calle")  
        calle_altura = data.get("calle_altura")
        telefono = data.get("telefono")  
        cliente = clientes(nombre=nombre, apellido=apellido, numero_cliente=numero_cliente, calle=calle, calle_altura=calle_altura, telefono=telefono)
        cliente.save()

        url_exitosa = reverse('lista_clientes')
        return redirect(url_exitosa)
    else: 
        return render(request, 'control_distr/formulario_cliente.html')
