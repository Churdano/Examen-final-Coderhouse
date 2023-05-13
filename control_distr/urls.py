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
from control_distr.views import  crear_cliente, buscar_cliente, buscar_producto, eliminar_producto
from control_distr.views import listar_productos,listar_clientes, listar_vendedores, eliminar_vendedor
from control_distr.views import crear_producto, buscar_vendedor, crear_vendedor, eliminar_cliente


urlpatterns = [
    path('productos/', listar_productos, name='lista_productos'),
    path('clientes/', listar_clientes, name='lista_clientes'),
    path('vendedores/', listar_vendedores, name='lista_vendedores'),
    path('crear-cliente/', crear_cliente, name='crear_cliente'),
    path('buscar-cliente/', buscar_cliente, name='buscar_cliente'),
    path('buscar-producto/', buscar_producto, name='buscar_producto'),
    path('crear-producto/', crear_producto, name='crear_producto'),
    path('buscar-vendedor/', buscar_vendedor, name='buscar_vendedor'),
    path('crear-vendedor/', crear_vendedor, name='crear_vendedor'),
    path('eliminar-cliente/<int:id>/', eliminar_cliente, name="eliminar_cliente"),
    path('eliminar-producto/<int:id>/', eliminar_producto, name="eliminar_producto"),
     path('eliminar-vendedor/<int:id>/', eliminar_vendedor, name="eliminar_vendedor"),

]