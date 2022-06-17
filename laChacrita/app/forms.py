from django import forms
from .models import Contacto, Producto, Calificacion, Donacion
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ProductoForm(forms.ModelForm):
    
    nombre = forms.CharField(min_length=3, label= ("Nombre del producto"))
    precio = forms.IntegerField(min_value=1000)
    imagen = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}), 
        required=False, 
        validators=[MaxSizeFileValidator(max_file_size=2)],
        label = 'Imagen del producto')
    
    class Meta:
        model = Producto
        fields = ["nombre", "categoria", "precio", "stock", "descripcion", "imagen"]
        
        widgets = {
            'descripcion' : forms.Textarea(attrs={
                'rows':5, 
                'cols':20,
                'minlength':20,
            }),
        }
        labels = {
            'categoria': 'Categor&iacute;a',
        }

class ContactoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=5)

    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "asunto", "mensaje", "checkOfertas"]

        widgets = {
            'mensaje' : forms.Textarea(attrs={
                'rows':5, 
                'cols':20,
                'minlength':20,
            }),
        }
        labels = {
            'correo': 'Correo electr&oacute;nico',
        }

class DonacionForm(forms.ModelForm):
    
    nombre = forms.CharField(min_length=5)
    monto = forms.IntegerField(min_value=1000)
    telefono = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': ('123456789'), 'pattern' : ("[0-9]{9}")}), 
        label= ("Tel&eacute;fono"))  

    class Meta:
        model = Donacion
        fields = ["nombre", "correo", "telefono", "monto", "tipoDonacion", "checkInforme"]

        labels = {
            'correo': 'Correo electr&oacute;nico',
            'checkInforme' : 'Recibir informacion al correo',
            'tipoDonacion' : 'Tipo de donaci&oacute;n'
        }


class CalificacionForm(forms.ModelForm):

    class Meta:
        model = Calificacion
        fields = ["usuario", "puntuacion", "comentario"]

        widgets = {
            'comentario' : forms.Textarea(attrs={
                'id':'comentario-txt',
                'minlength':'20',
                'rows':5, 
                'cols':20,
            }),
        }
        labels = {
            'usuario': 'Usuario'
        }