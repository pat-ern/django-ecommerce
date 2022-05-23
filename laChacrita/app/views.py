from errno import EADDRNOTAVAIL
from django.shortcuts import render
from .models import Producto

# INDEX

def index(request):
    productos = Producto.objects.all()
    data = {
        "productos" : productos
    }
    return render(request, 'app/index.html', data)

# PRODUCTO
def producto(request):
    return render(request, 'app/producto.html')

# CONOCENOS
def conocenos(request):
    return render(request, 'app/conocenos.html')

# CONTACTO
def contacto(request):
    return render(request, 'app/contacto.html')

# DONACIONES
def donaciones(request):
    return render(request, 'app/donaciones.html')