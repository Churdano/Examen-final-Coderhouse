from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class clientes(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    calle_altura = models.IntegerField()
    telefono = models.CharField(max_length=200)
    numero_cliente = models.IntegerField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    
    
class productos(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    
class vendedor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
