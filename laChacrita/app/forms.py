from cProfile import label
from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "mensaje", "checkOfertas", "asunto"]
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ["nombre", "categoria", "precio", "descripcion", "imagen"]
        
        widgets = {
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'lorem ipsum',
            }),
        }
        labels = {
            'imagen': 'Imagen del producto',
        }