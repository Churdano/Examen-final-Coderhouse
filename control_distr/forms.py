from django import forms
from .models import clientes, productos

class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = '__all__'
    
class VendedorForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
