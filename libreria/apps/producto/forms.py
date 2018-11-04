from django import forms
from apps.producto.models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto

        fields = [
            'nombre',
            'tipo',
            'descripcion',
            'precio',
            'cantidad',
            'codigo',
        ]

        label = {
            'nombre' : 'Nombre',
            'tipo' : 'Tipo',
            'descripcion' : 'Descripción',
            'precio' : 'Precio',
            'cantidad' : 'Cantidad',
            'codigo' : 'Código',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'input-field'}),
            'precio': forms.TextInput(attrs={'class':'input-field'}),
            'cantidad': forms.TextInput(attrs={'class':'input-field'}),
            'codigo': forms.TextInput(attrs={'class':'input-field'}),
        }