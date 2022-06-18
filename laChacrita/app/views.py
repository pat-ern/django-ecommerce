from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView

from rest.serializers import SuscripcionSerializer

from .filters import IndexFilter
from .forms import ContactoForm, ProductoForm, CalificacionForm, SuscripcionForm
from .models import Calificacion, Producto
from .customers import calcular_promedio
import requests

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status 

# INDEX
class FilteredIndex(ListView):
    
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        filter = IndexFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = filter
        return context

class Index(FilteredIndex):

    model = Producto
    filterset_class = IndexFilter
    paginate_by= 6
    template_name= 'app/index.html'

# PRODUCTO

def producto(request, id):
    
    calificaciones = Calificacion.objects.filter(idProducto=id).order_by('-id')
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'producto' : producto,
        'form': CalificacionForm(),
        'calificaciones': calificaciones
    }

    if request.method == 'POST':

        formulario = CalificacionForm(data=request.POST)
        if formulario.is_valid():
            # se actualiza registro en modelo
            calificacion = formulario.save(commit=False) 
            calificacion.idProducto = producto.id 
            calificacion.save()

            # promedio calificaciones y actualizacion de producto
            puntuaciones = Calificacion.objects.values_list('puntuacion', flat=True).filter(idProducto=id)
            prod = Producto.objects.get(id=id)
            prod.puntuacion_avg = calcular_promedio(puntuaciones)
            prod.save()

            data["producto"] = prod

        else:
            data["form"] = formulario

    return render(request, 'app/producto.html', data)

# AGREGAR PRODUCTO
def agregarProducto(request):
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tu producto se agregó correctamente.")
            return redirect(to="index")
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/agregar.html', data)

# LISTAR
def listarProducto(request):
    productos = Producto.objects.all().order_by('-id')
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

# MODIFICAR
def modificarProducto(request, id):
    
    producto = get_object_or_404(Producto,id=id)
    
    data = {
        'form': ProductoForm(instance=producto),
        'producto' : producto
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

# ELIMINAR
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
            return redirect(to="index")
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

# SUSCRIPCION
def suscripcion(request):
    data = {
        'form': SuscripcionForm()
    }
    if request.method == 'POST':
        formulario = SuscripcionForm(data=request.POST)
        if formulario.is_valid():
            url = "http://127.0.0.1:8000/api/lista_suscripcion"
            requests.post(url, json=request.POST)
            messages.success(request, "¡Gracias por tu donación!")
            return redirect(to="index")
        else:
            data['form'] = formulario
     
    return render(request, 'app/suscripcion.html', data)

# LISTAR SUSCRIPCIONES (REST)
def suscripciones(request):
    url = "http://127.0.0.1:8000/api/lista_suscripcion"
    response = requests.get(url).json()
    data = {
        'suscripciones' : response
    }
    return render(request, 'app/suscripciones/listar.html', data)