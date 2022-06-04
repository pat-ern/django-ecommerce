from errno import EADDRNOTAVAIL
from django.shortcuts import redirect, render, get_object_or_404
from .models import CategoriaProducto, FiltroPrecios, Producto
from django.core.paginator import Paginator
from django.http import Http404
from .forms import ContactoForm, ProductoForm
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView

# INDEX

def index(request):
    
    categorias = CategoriaProducto.objects.all()
    precios = FiltroPrecios.objects.all()
    
    #
    unchecked = request.GET.get('result', None)
    print(unchecked)
    #
    productos = Producto.objects.exclude(categoria=unchecked)
    print(len(productos))

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 6)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        "productos" : productos,
        "paginator" : paginator,
        "categorias" : categorias,
        "precios" : precios
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
def listarProducto(request):
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
    
    return render(request, 'app/producto/listar.html', data)

# CONOCENOS > MODIFICAR
def modificarProducto(request, id):
    
    producto = get_object_or_404(Producto,id=id)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tu producto se modificó correctamente.")
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/modificar.html', data)

# CONOCENOS > ELIMINAR
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)    
    producto.delete()
    messages.success(request, "Producto eliminado correctamente.")
    return redirect(to="listar_producto")


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