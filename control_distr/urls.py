"""
URL configuration for Distribuidora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from control_distr.views import listar_productos, listar_clientes, crear_cliente, buscar_clientes

urlpatterns = [
    path('productos/', listar_productos, name='lista_productos'),
    path('clientes/', listar_clientes, name='lista_clientes'),
    path('crear-cliente/', crear_cliente, name='crear_clientes'),
    path('buscar-cliente/', buscar_clientes, name='buscar_clientes'),
]