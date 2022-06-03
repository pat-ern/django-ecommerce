from errno import EADDRNOTAVAIL
from django.shortcuts import redirect, render, get_object_or_404
from .models import CategoriaProducto, FiltroPrecios, Producto, Snippet
from django.core.paginator import Paginator
from django.http import Http404
from .forms import ContactoForm, ProductoForm
from django.contrib import messages
from django.urls import reverse
from .filters import SnippetFilter
from django.views.generic import ListView, DetailView
from django.views import View

class SnippetListView(ListView):
    
    model = Snippet
    template_name = 'app/snippet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        return context

class SnippetDetailView(DetailView):

    model = Snippet
    template_name = 'app/snippet_detail.html'


# INDEX
def index(request):
    
    categorias = CategoriaProducto.objects.all()
    precios = FiltroPrecios.objects.all()
    productos = Producto.objects.all()

    arr0 = [1,2,3,4,5]
    arr0.remove(1) # categoria por id que deseo mostrar

    productos = Producto.objects.exclude(categoria__in=arr0)
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