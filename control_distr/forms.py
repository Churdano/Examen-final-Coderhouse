from django import forms
from .models import clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'
    
class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=300)
    precio = forms.IntegerField()
    
class VendedorForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
