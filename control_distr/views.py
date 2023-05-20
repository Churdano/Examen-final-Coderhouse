from django.shortcuts import render, redirect
from django.urls import reverse
from control_distr.models import productos, clientes, vendedor
from .forms import ProductoForm, ClienteForm, VendedorForm


def saludar_con_html(request):
    contexto = {
        'saludo': 'Bienvenido a distribuidora LG!',
    }
    return render(request, 'control_distr/inicio.html', contexto)



#cliente
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

def buscar_cliente(request):
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

def eliminar_cliente(request, id):
   cliente = clientes.objects.get(id=id)
   if request.method == "POST":
       cliente.delete()
       url_exitosa = reverse('lista_clientes')
       return redirect(url_exitosa)
   
def editar_cliente(request, id):
   cliente = clientes.objects.get(id=id)
   if request.method == "POST":
       formulario = ClienteForm(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           cliente.nombre = data['nombre']
           cliente.apellido = data['apellido']
           cliente.numero_cliente = data['numero_cliente']
           cliente.calle = data['calle']
           cliente.calle_altura = data['calle_altura']
           cliente.telefono = data['telefono']
           cliente.save()
           url_exitosa = reverse('lista_clientes')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': cliente.nombre,
           'apellido': cliente.apellido,
           'numero_cliente': cliente.numero_cliente,
           'calle': cliente.calle,
           'calle_altura': cliente.calle_altura,
           'telefono': cliente.telefono,
       }
       formulario = ClienteForm(initial=inicial)
   return render(
        request=request,
        template_name='control_distr/formulario_cliente.html',
        context={'form': formulario},
   )


#producto
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

def listar_productos(request):
    contexto = {
        "productos": productos.objects.all(),
    }
    return render(request, 'control_distr/lista_productos.html', contexto)

def buscar_producto(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        resultados = productos.objects.filter(nombre__contains=busqueda)
        contexto = {
            "productos": resultados,
        }
        return render(request, 'control_distr/lista_productos.html', contexto)

def eliminar_producto(request, id):
   producto = productos.objects.get(id=id)
   if request.method == "POST":
       producto.delete()
       url_exitosa = reverse('lista_productos')
       return redirect(url_exitosa)

def editar_producto(request, id):
   producto = productos.objects.get(id=id)
   if request.method == "POST":
       formulario = ProductoForm(request.POST, instance=producto)

       if formulario.is_valid():
           data = formulario.cleaned_data
           producto.nombre = data['nombre']
           producto.precio = data['precio']
           producto.save()
           url_exitosa = reverse('lista_productos')
           return redirect(url_exitosa)
   else:  # GET
       formulario = ProductoForm(instance=producto)
   return render(
        request=request,
        template_name='control_distr/formulario_producto.html',
        context={'form': formulario},
   )


#vendedor    
def listar_vendedores(request):
    contexto = {
        "vendedores": vendedor.objects.all(),
    }
    return render(request, 'control_distr/lista_vendedores.html', contexto)

def crear_vendedor(request):
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            resultado = vendedor(nombre=nombre, apellido=apellido)
            resultado.save()
            url_exitosa = reverse('lista_vendedores')
            return redirect(url_exitosa)
    else:
        form = VendedorForm()
    
    contexto = {
        'form': form
    }
    return render(request, 'control_distr/formulario_vendedor.html', contexto)

def buscar_vendedor(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        resultados = vendedor.objects.filter(apellido__contains=busqueda)
        contexto = {
            "vendedores": resultados,
        }
        return render(request, 'control_distr/lista_vendedores.html', contexto)

def eliminar_vendedor(request, id):
   vendedores = vendedor.objects.get(id=id)
   if request.method == "POST":
       vendedores.delete()
       url_exitosa = reverse('lista_vendedores')
       return redirect(url_exitosa)
