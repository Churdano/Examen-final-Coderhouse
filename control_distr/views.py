from django.shortcuts import render
from control_distr.models import productos, clientes

def saludar_con_html(request):
    contexto = {
        'saludo': 'Bienvenido a distribuidora LG!',
    }
    HttpResponse = render(
        request=request,
        template_name='control_distr/inicio.html',
        context=contexto,
    )
    
    return HttpResponse

def listar_productos(request):
    contexto = {
        "productos": productos.objects.all(),
    }
    HttpResponse = render(
        request=request,
        template_name='control_distr/lista_productos.html',
        context=contexto,
    )
    
    return HttpResponse
    
    
def listar_clientes(request):
    contexto = {
        "clientes": clientes.objects.all(),
    }
    HttpResponse = render(
        request=request,
        template_name='control_distr/lista_clientes.html',
        context=contexto,
    )
    
    return HttpResponse

def crear_cliente(request):
    contexto = {}
    HttpResponse = render(
        request=request,
        template_name='control_distr/formulario_cliente.html',
        context=contexto,
    )
    
    return HttpResponse