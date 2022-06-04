from cProfile import label
from django import forms
from .models import Contacto, Producto, Calificacion

class ContactoForm(forms.ModelForm):

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

class CalificacionForm(forms.ModelForm):

    class Meta:
        model = Calificacion
        fields = ["usuario", "puntuacion", "comentario"]

        widgets = {
            'comentario' : forms.Textarea(attrs={
                'rows':5, 
                'cols':20
            }),
        }
        labels = {
            'usuario': 'Usuario'
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