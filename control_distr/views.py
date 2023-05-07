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
    