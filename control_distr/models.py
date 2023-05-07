from django.db import models

# Create your models here.

class clientes(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    calle_altura = models.IntegerField()
    telefono = models.CharField(max_length=200)
    numero_cliente = models.IntegerField()
    
    
class productos(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    
class vendedor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    
    
class pedidos(models.Model):
    fecha_pedido = models.DateField()
    aprobado = models.BooleanField(default=False)