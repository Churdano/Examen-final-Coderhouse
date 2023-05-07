from django.shortcuts import render
from django.http import HttpResponse

def saludar_con_html(request):
    contexto = {}
    HttpResponse = render(
    request = request,
    template_name = 'control_distr/base.html',
    context = contexto,
    )
    
    return HttpResponse

def listar_productos(request):
    contexto = {
        "productos": [
            {"nombre" : "Destornillador", "precio" : "500"},
        ]
    }
    HttpResponse = render(
    request = request,
    template_name = 'control_distr/lista_productos.html',
    context = contexto,
    )
    
    return HttpResponse
    
    
def listar_clientes(request):
    contexto = {
        "clientes": [
            {"nombre" : "Pepe", "numero_cliente" : "1"},
        ]
    }
    HttpResponse = render(
    request = request,
    template_name = 'control_distr/lista_clientes.html',
    context = contexto,
    )
    
    return HttpResponse