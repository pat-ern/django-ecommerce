from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from rest_framework.authtoken.models import Token

from .filters import IndexFilter
from .forms import ContactoForm, DetalleCarritoForm, EstadoSuscripcionForm, ProductoForm, CalificacionForm, SuscripcionForm, CustomUserCreationForm
from .models import Calificacion, Compra, DetalleCarrito, DetalleCompra, Pedido, Producto, Suscripcion
from .operaciones import calcular_promedio
import requests

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
        'calificaciones': calificaciones,
        'carritoForm' : DetalleCarritoForm(),
    }

    # ANADIR AL CARRITO
    if request.method == 'POST':
        formulario = DetalleCarritoForm(data=request.POST)

        if formulario.is_valid():
            cart = formulario.save(commit=False)
            cart.comprador = request.user
            cart.producto = producto
            cart.subtotal = cart.cantidad * producto.precio
            cart.save()
            
            messages.success(request, "Se ha añadido al carrito correctamente.")
            return redirect(to="producto", id=id)

    # CALIFICACION
    if request.method == 'POST':
        formulario = CalificacionForm(data=request.POST)

        if formulario.is_valid():
            calificacion = formulario.save(commit=False) 
            calificacion.idProducto = producto.id 
            calificacion.usuario = request.user
            calificacion.save()

            # promedio calificaciones y actualizacion de producto
            puntuaciones = Calificacion.objects.values_list('puntuacion', flat=True).filter(idProducto=id)
            prod = Producto.objects.get(id=id)
            prod.puntuacion_avg = calcular_promedio(puntuaciones)
            prod.save()

        else:
            data["form"] = formulario

    return render(request, 'app/producto.html', data)

def eliminar_calificacion(request, id):
    # eliminar calificacion
    calificacion = get_object_or_404(Calificacion, id=id)    
    calificacion.delete()

    puntuaciones = Calificacion.objects.values_list('puntuacion', flat=True).filter(idProducto=calificacion.idProducto)
    producto = Producto.objects.get(id=calificacion.idProducto)

    if len(puntuaciones) == 0:
        producto.puntuacion_avg = 0
    else:
        producto.puntuacion_avg = calcular_promedio(puntuaciones)
    
    producto.save()

    messages.success(request, "Calificacion eliminada.")
    return redirect(to="producto", id=calificacion.idProducto)

# AGREGAR PRODUCTO\
@permission_required('app.add_producto')
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

# LISTA
@permission_required('app.view_producto')
def lista_productos(request):
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
@permission_required('app.change_producto')
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
            return redirect(to="lista_productos")
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/modificar.html', data)

# ELIMINAR
@permission_required('app.delete_producto')
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)    
    producto.delete()
    messages.success(request, "Producto eliminado correctamente.")
    return redirect(to="lista_productos")

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

# --------------------------CONSUMO DE API--------------------------

# CREAR SUSCRIPCION (REST)
@login_required
def crear_suscripcion(request):

    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    # Consultar suscripciones
    url_lista = "http://127.0.0.1:8000/api/lista_suscripcion"
    suscripciones = requests.get(url_lista, headers=headers).json()

    data = {
        'form': SuscripcionForm()
    }

    # Buscar si usuario esta suscrito y obtener suscripcion
    for i in suscripciones:
        if i['suscriptor'] == request.user.id:
            id = i['id']
            url2 = f'http://127.0.0.1:8000/api/detalle_suscripcion/{id}'
            data['suscripcion'] = requests.get(url2, headers=headers).json()

    if request.method == 'POST':
        formulario = SuscripcionForm(data=request.POST)

        if formulario.is_valid():
            copia_dict = request.POST.copy()
            copia_dict['suscriptor'] = request.user.id
            requests.post(url_lista, headers=headers, json=copia_dict)
            messages.success(request, "Gracias por suscribirte.")
            return redirect(to="index")

        else:
            data['form'] = formulario

    return render(request, 'app/suscripcion.html', data)

# LISTAR SUSCRIPCIONES (REST)
@login_required
def lista_suscripciones(request):

    url = "http://127.0.0.1:8000/api/lista_suscripcion"
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    suscripciones = requests.get(url, headers=headers).json()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(suscripciones, 5)
        suscripciones = paginator.page(page)
    except:
        raise Http404

    data = {
        'suscripciones' : suscripciones,
        "paginator" : paginator
    }

    return render(request, 'app/suscripciones/listar.html', data)

# CANCELAR SUSCRIPCION (REST)
@login_required
def cancelar_suscripcion(request, id): 

    url = f'http://127.0.0.1:8000/api/detalle_suscripcion/{id}'
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    requests.delete(url, headers=headers)
    messages.success(request, "Suscripcion cancelada.")
    
    return redirect(to="lista_suscripciones")

# MODIFICAR SUSCRIPCION (REST)
@login_required
def modificar_suscripcion(request, id): 

    url = f'http://127.0.0.1:8000/api/detalle_suscripcion/{id}'
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    suscripcion = requests.get(url, headers=headers).json()
    
    data = {
        'form' : SuscripcionForm(data=suscripcion)
    }

    if request.method == 'POST':
        formulario = SuscripcionForm(data=request.POST)
        if formulario.is_valid():
            requests.put(url, headers=headers, json=request.POST)
            messages.success(request, "Calificacion modificada.")
            return redirect(to="lista_suscripciones")
        else:
            data["form"] = formulario
    
    return render(request, 'app/suscripciones/modificar.html', data)

# MODIFICAR SOLO ESTADO DE SUSCRIPCION (REST)
@login_required
def estado_suscripcion(request, id): 

    url = f'http://127.0.0.1:8000/api/detalle_suscripcion/{id}'
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    suscripcion = requests.get(url, headers=headers).json()
    
    data = {
        'form' : EstadoSuscripcionForm(data=suscripcion),
        'suscripcion' : suscripcion
    }

    suscripcion['estado'] = request.POST.get('estado')

    if request.method == 'POST':
        formulario = EstadoSuscripcionForm(data=request.POST)
        if formulario.is_valid():
            requests.put(url, headers=headers, json=suscripcion)
            messages.success(request, "Estado actualizado.")
            return redirect(to="lista_suscripciones")
        else:
            data["form"] = formulario
    
    return render(request, 'app/suscripciones/cambiar_estado.html', data)

# -------------------------- LOGIN Y REGISTRO --------------------------

# LOGIN (REST)
def inicio_sesion(request):

    data = {
        'form' : AuthenticationForm
        #'user' : request.user
    }

    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)

        if formulario.is_valid():
            url = "http://127.0.0.1:8000/api/login"
            requests.post(url, json=request.POST)
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password"])
            login(request, user)
            return redirect(to="index")
        else:
            data['form'] = formulario

    return render(request, 'registration/iniciosesion.html', data)

# REGISTRO USUARIO
def registro_usuario(request):

    data = {
        'form' : CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente.")
            return redirect(to='index')
        data['form'] = formulario


    return render(request, 'registration/registro.html', data)

# CARRITO DE COMPRAS

def carrito_compras(request):

    carrito = DetalleCarrito.objects.filter(comprador = request.user)

    # contar cantidad de productos en carrito
    cant = 0
    for i in carrito:
        cant += i.cantidad

    # calcular total
    total = 0
    for i in carrito:
        total += i.subtotal

    data = {
        'carrito' : carrito,
        'total' : total,
        'cantidad' : cant
    }

    return render(request, 'app/usuario/carrito.html', data)

def eliminar_de_carrito(request, id):
    detalle_carrito = get_object_or_404(DetalleCarrito, id=id)    
    detalle_carrito.delete()
    messages.success(request, "Producto eliminado del carrito.")
    return redirect(to="carrito")

def detalle_compra(request):

    carrito = DetalleCarrito.objects.filter(comprador = request.user)

    total = 0
    for i in carrito:
        total += i.subtotal

    data = {
        'carrito' : carrito,
        'total' : total
    }

    # Falta generar descuento
    descuento = 0

    if(request.GET.get('comprar')):

        # Crear compra
        compra = Compra.objects.create(comprador = request.user, total = total)
        compra.descuento = descuento
        compra.valor_final = total - descuento
        compra.save()

        # Crear detalle compra
        for i in carrito:
            detalle_compra = DetalleCompra.objects.create(compra = compra, producto = i.producto, cantidad = i.cantidad, subtotal = i.subtotal)
            detalle_compra.save()

        # Generar pedido de compra
        Pedido.objects.create(compra = compra)

        # Descontar productos del inventario
        for i in carrito:
            producto = get_object_or_404(Producto, id=i.producto.id)
            producto.stock -= i.cantidad
            producto.save()

        # Eliminar carrito
        for i in carrito:
            i.delete()
            
        messages.success(request, "Compra realizada.")
        return redirect(to="index")

    return render(request, 'app/compra/detallecompra.html', data)