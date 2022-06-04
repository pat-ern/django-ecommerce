from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView

from .filters import IndexFilter
from .forms import ContactoForm, ProductoForm, CalificacionForm
from .models import Calificacion, Producto

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
    comentarios = Calificacion.objects.filter(idProducto=id).order_by('-id')
    producto = get_object_or_404(Producto, id=id)
    data = {
        'producto' : producto,
        'form': CalificacionForm(),
        'comentarios': comentarios
    }

    if request.method == 'POST':
        formulario = CalificacionForm(data=request.POST)
        if formulario.is_valid():
            obj = formulario.save(commit=False)
            obj.idProducto = producto.id
            obj.save()
            messages.success(request, "Comentario enviado.")
            def handler404(request, *args, **argv):
                return redirect('producto')
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
            return redirect(to="modificar_producto")
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

# DONACIONES
def donaciones(request):
    return render(request, 'app/donaciones.html')