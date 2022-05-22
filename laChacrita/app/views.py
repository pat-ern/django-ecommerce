from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def producto(request):
    return render(request, 'app/producto.html')

def conocenos(request):
    return render(request, 'app/conocenos.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def donaciones(request):
    return render(request, 'app/donaciones.html')