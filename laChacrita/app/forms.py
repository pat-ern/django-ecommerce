from django import forms
from .models import Contacto, Producto, Calificacion, Donacion

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
    
    nombre = forms.CharField(min_length=5, widget=forms.TextInput(
        attrs={'id':'nombre'}))

    correo = forms.CharField(widget= forms.EmailInput(
        attrs={'id':'correo'}))

    #telefono = forms.IntegerField(widget=forms.NumberInput(
    #    attrs={'id':'telefono', 'placeholder': ('123456789'), 'pattern' : ("[0-9]{9}")}), 
    #    label= ("Tel&eacute;fono"))  

    monto = forms.IntegerField(widget=forms.TextInput(
        attrs={'type':'number','id':'monto', 'min':'1000'}))

    class Meta:
        model = Donacion
        fields = ["nombre", "correo", "telefono", "monto", "tipoDonacion", "checkInforme"]

        widgets = {
            'telefono' : forms.TextInput(attrs={
                'type':'tel',
                'id':'telefono',
                'placeholder':('123456789'),
                'pattern':'([0-9]{9})'
            }),
        }
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