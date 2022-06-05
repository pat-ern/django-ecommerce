from django import forms
from .models import Contacto, Producto, Calificacion, Donacion

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
                'id':'comentario-txt',
                'rows':5, 
                'cols':20,
            }),
        }
        labels = {
            'usuario': 'Usuario'
        }
        
class ProductoForm(forms.ModelForm):
    
    nombre = forms.CharField(min_length=3, label= ("Nombre del producto"))
    precio = forms.IntegerField(min_value=1000)
    
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
                'cols':20,
                'minlength':20,
            }),
        }
        labels = {
            'imagen': 'Imagen del producto',
            'categoria': 'Categor&iacute;a',
        }

class DonacionForm(forms.ModelForm):
    
    nombre = forms.CharField(min_length=3, label= ("Nombre y apellido"))
    monto = forms.IntegerField(min_value=1000)
    celular = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': ('123456789'), 'pattern' : ('[0-9]{9}')}), 
        label= ("Tel&eacute;fono"))
        
    class Meta:
        model = Donacion
        fields = ["nombre", "correo", "celular", "monto", "tipoDonacion", "checkInforme"]

        labels = {
            'correo': 'Correo electr&oacute;nico',
            'checkInforme' : 'Recibir informacion al correo',
            'tipoDonacion' : 'Tipo de donaci&oacute;n'
        }