from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Contacto, DetalleCarrito, Pedido, Producto, Calificacion, Suscripcion
from .validators import MaxSizeFileValidator

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

class SuscripcionForm(forms.ModelForm):

    class Meta:
        model = Suscripcion
        fields = ["tipo_suscripcion", "recibe_informe"]

        labels = {
            'recibe_informe' : 'Recibir informacion al correo',
            'tipo_suscripcion' : 'Tipo de suscripci&oacute;n',
        }

class EstadoSuscripcionForm(forms.ModelForm): 

    class Meta:
        model = Suscripcion
        fields = ["estado"]

        labels = {
                'estado' : 'Suscripcion activa'
            }


class CalificacionForm(forms.ModelForm):

    class Meta:
        model = Calificacion
        fields = ["puntuacion", "comentario"]

        widgets = {
            'comentario' : forms.Textarea(attrs={
                'id':'comentario-txt',
                'minlength':'20',
                'rows':5, 
                'cols':20,
            }),
        }

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class DetalleCarritoForm(forms.ModelForm):

    class Meta:
        model = DetalleCarrito
        fields = ["cantidad"]

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ["estado"]

        labels = {
                'estado' : 'Cambiar estado del pedido'
            }