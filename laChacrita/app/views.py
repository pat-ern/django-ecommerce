from errno import EADDRNOTAVAIL
from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
from django.core.paginator import Paginator
from django.http import Http404
from .forms import ContactoForm, ProductoForm
from django.contrib import messages

# INDEX

def index(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 6)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
        "productos" : productos,
        "paginator" : paginator
    }
    return render(request, 'app/index.html', data)

# PRODUCTO
def producto(request, id):
    prod = get_object_or_404(Producto, id=id)
    data = {
        'producto' : prod
    }
    return render(request, 'app/producto.html', data)

# CONOCENOS
def agregarProducto(request):
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tu producto se agregó correctamente.")
            #data["mensaje"] = "Contacto enviado."
            return redirect(to="index")
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/agregar.html', data)

# CONOCENOS
def modificarProducto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        "productos" : productos,
        "paginator" : paginator
    }
    
    return render(request, 'app/producto/modificar.html', data)

# CONOCENOS
def conocenos(request):
    return render(request, 'app/conocenos.html')

# CONTACTO
def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Gracias por contactarte con nosotros")
            #data["mensaje"] = "Contacto enviado."
            return redirect(to="index")
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

# DONACIONES
def donaciones(request):
    return render(request, 'app/donaciones.html')