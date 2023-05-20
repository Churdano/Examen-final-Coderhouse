from django import forms
from .models import clientes, productos, vendedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = '__all__'
    
class VendedorForm(forms.ModelForm):
    class Meta:
        model = vendedor
        fields = '__all__'
