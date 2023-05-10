from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    numero_cliente = forms.IntegerField()
    calle = forms.CharField(max_length=100)
    calle_altura = forms.IntegerField()
    telefono = forms.IntegerField()
    
class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=300)
    precio = forms.IntegerField()
