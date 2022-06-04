from cProfile import label
from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "mensaje", "checkOfertas", "asunto"]

        widgets = {
            'mensaje' : forms.Textarea(attrs={
                'rows':5, 
                'cols':20
            }),
        }
        labels = {
            'nombre': 'Nombre y apellido',
            'correo': 'Correo electr&oacute;nico',
        }
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ["nombre", "categoria", "precio", "descripcion", "imagen"]
        
        widgets = {
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'lorem ipsum',
            }),
            'descripcion' : forms.Textarea(attrs={
                'rows':5, 
                'cols':20
            }),
        }
        labels = {
            'nombre': 'Nombre del producto',
            'imagen': 'Imagen del producto',
        }