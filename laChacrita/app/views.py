from datetime import datetime
from django.dispatch import receiver
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .filters import IndexFilter
from .forms import ContactoForm, DetalleCarritoForm, EstadoSuscripcionForm, PedidoForm, ProductoForm, CalificacionForm, SuscripcionForm, CustomUserCreationForm
from .models import Calificacion, Compra, DetalleCarrito, DetalleCompra, EstadoPedido, HistorialEstadoPedido, Pedido, Producto
from .operaciones import calcular_promedio
import requests
from allauth.account.signals import user_logged_in

# Funcion que se trigerea despues de cualquier login
@receiver(user_logged_in, dispatch_uid="unique")
def user_logged_in_(request, user, **kwargs):
    Token.objects.get_or_create(user = user)

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

    # Se obtiene el producto
    producto = get_object_or_404(Producto, id=id)

    # Se obtienen las calificaciones del producto
    calificaciones = Calificacion.objects.filter(idProducto=id).order_by('-id')

    # Se pasan datos al template
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
            # Se realiza copia del formulario
            cart = formulario.save(commit=False)
            # Se valida que el producto tenga el stock requerido
            if cart.cantidad > producto.stock:
                messages.error(request, "No hay suficientes unidades disponibles.", extra_tags='Error')
                return redirect(to='producto', id=id)
            else:
                # Se termina de guardar el formulario
                cart.comprador = request.user
                cart.producto = producto
                cart.subtotal = cart.cantidad * producto.precio
                cart.save()
                
                messages.success(request, "Se ha añadido al carrito correctamente.", extra_tags='Agregado')
                return redirect(to="producto", id=id)

    # CALIFICACION
    if request.method == 'POST':
        formulario = CalificacionForm(data=request.POST)

        if formulario.is_valid():
            # Se realiza copia del formulario para agregar otros campos
            calificacion = formulario.save(commit=False) 
            calificacion.idProducto = producto.id 
            calificacion.usuario = request.user
            calificacion.save()

            # Se obtienen las calificaciones del producto como lista de enteros
            puntuaciones = Calificacion.objects.values_list('puntuacion', flat=True).filter(idProducto=id)
            # Se calcula el promedio y se guarda en el producto
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

    messages.info(request, "Calificacion eliminada.", extra_tags="Eliminada")
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
            messages.success(request, "Tu producto se agregó correctamente.", extra_tags='Agregado')
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
            messages.success(request, "El producto se modificó correctamente.", extra_tags='Modificado')
            return redirect(to="lista_productos")
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/modificar.html', data)

# ELIMINAR
@permission_required('app.delete_producto')
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)    
    producto.delete()
    messages.info(request, "Producto eliminado correctamente.", extra_tags='Eliminado')
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
            messages.success(request, "Gracias por contactarte con nosotros", extra_tags='Enviado')
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
            url_detalle = f'http://127.0.0.1:8000/api/detalle_suscripcion/{id}'
            data['suscripcion'] = requests.get(url_detalle, headers=headers).json()

    if request.method == 'POST':
        formulario = SuscripcionForm(data=request.POST)

        if formulario.is_valid():
            copia_dict = request.POST.copy()
            copia_dict['suscriptor'] = request.user.id
            requests.post(url_lista, headers=headers, json=copia_dict)
            messages.success(request, "Gracias por ser parte de esta fundacion.", extra_tags='Suscrito')
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
    messages.info(request, "Esperamos tenerte de vuelta pronto.", extra_tags='Suscripcion Cancelada')
    
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
            messages.success(request, "La suscripcion se ha modificado correctamente.", extra_tags='Modificada')
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
            messages.success(request, "Estado de suscripcion modificado correctamente", extra_tags='Estado actualizado')
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
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()

            #user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            #login(request, user)

            messages.success(request, "Te has registrado correctamente.", extra_tags='Registrado')
            return redirect(to='inicio_sesion')
        data['form'] = formulario


    return render(request, 'registration/registro.html', data)

# CARRITO DE COMPRAS

def carrito_compras(request):

    # Se obtiene total de productos en el carrito de usuario
    carrito = DetalleCarrito.objects.filter(comprador = request.user)

    # Contar cantidad de productos en carrito
    cant = 0
    for i in carrito:
        cant += i.cantidad

    # Calcular total
    total = 0
    for i in carrito:
        total += i.subtotal#*i.cantidad (subtotal es igual al precio unitario * cantidad)
        
    # Calcular descuento en carrito de compras
    token = Token.objects.get(user=request.user) 
    # Se pasa token al header
    headers = {'Authorization': f'Token {token}'}
    url_lista = "http://127.0.0.1:8000/api/lista_suscripcion" 
    # Se realiza consulta a api fundacion
    suscripciones = requests.get(url_lista, headers=headers).json() 

    # Inicializadores
    porc_descuento = 0
    descuento = 0
    final_a_pagar = 0

    # Buscar si usuario esta suscrito, obtener suscripcion, generar descuento
    # Iteracion dentro de suscripciones obtenidas
    for i in suscripciones:
        if i['suscriptor'] == request.user.id:
            # Se obtiene id de suscripcion
            id = i['id']
            # Se consulta a la api por suscripcion
            url_detalle = f'http://127.0.0.1:8000/api/detalle_suscripcion/{id}'
            sub = requests.get(url_detalle, headers=headers).json()
            # Consultar tipo de suscripcion
            if sub['tipo_suscripcion'] == 1:
                porc_descuento = 5
            elif sub['tipo_suscripcion'] == 2:
                porc_descuento = 8
            elif sub['tipo_suscripcion'] == 3:
                porc_descuento = 10
            # Generar descuento
            descuento = round(total * (porc_descuento/100))
            break

    final_a_pagar = total - descuento

    data = {
        'carrito' : carrito,
        'total' : total,
        'cantidad' : cant,
        'descuento' : descuento,
        'final_a_pagar' : final_a_pagar,
    }

    return render(request, 'app/compra/carrito.html', data)

def eliminar_de_carrito(request, id):
    # Se obtiene el producto a eliminar
    detalle_carrito = get_object_or_404(DetalleCarrito, id=id)  
    # Se elimina el producto del carrito  
    detalle_carrito.delete()
    messages.info(request, "Producto eliminado del carrito.", extra_tags="Eliminado")
    return redirect(to="carrito")

def compra(request):

    # Calculo de total
    carrito = DetalleCarrito.objects.filter(comprador = request.user)

    total = 0
    for i in carrito:
        total += i.subtotal#*i.cantidad (subtotal es igual al precio unitario * cantidad)

    # Se consigue token de usuario
    token = Token.objects.get(user=request.user) 
    # Se pasa token al header
    headers = {'Authorization': f'Token {token}'}
    url_lista = "http://127.0.0.1:8000/api/lista_suscripcion" 
    # Se realiza consulta a api fundacion
    suscripciones = requests.get(url_lista, headers=headers).json() 

    # Inicializadores
    porc_descuento = 0
    descuento = 0
    tipo_suscriptor = "Sin suscripcion"

    # Buscar si usuario esta suscrito, obtener suscripcion, generar descuento
    # Iteracion dentro de suscripciones obtenidas
    for i in suscripciones:
        if i['suscriptor'] == request.user.id:
            # Se obtiene id de suscripcion
            id = i['id']
            # Se consulta a la api por suscripcion
            url_detalle = f'http://127.0.0.1:8000/api/detalle_suscripcion/{id}'
            sub = requests.get(url_detalle, headers=headers).json()
            # Consultar tipo de suscripcion
            if sub['tipo_suscripcion'] == 1:
                porc_descuento = 5
                tipo_suscriptor = "Basic"
            elif sub['tipo_suscripcion'] == 2:
                porc_descuento = 8
                tipo_suscriptor = "Standard"
            elif sub['tipo_suscripcion'] == 3:
                porc_descuento = 10
                tipo_suscriptor = "Premium"
            # Generar descuento
            descuento = round(total * (porc_descuento/100))
            break

    final_a_pagar = total - descuento

    # Se pasan variables al contexto
    data = {
        'carrito' : carrito,
        'total' : total,
        'porc_descuento' : porc_descuento,
        'tipo_suscriptor' : tipo_suscriptor,
        'final_a_pagar' : final_a_pagar,
        'descuento' : descuento,
    }

    # Click boton comprar
    if(request.GET.get('comprar')):

        # Crear compra
        compra = Compra.objects.create(comprador = request.user, total = total)
        compra.descuento = descuento
        compra.valor_final = final_a_pagar
        compra.save()

        # Crear detalle compra
        for i in carrito:
            detalle_compra = DetalleCompra.objects.create(compra = compra, producto = i.producto, cantidad = i.cantidad, subtotal = i.subtotal)
            detalle_compra.save()

        # Generar pedido de compra
        pedido = Pedido.objects.create(compra = compra)
        pedido.actualizacion = datetime.now()
        pedido.save()

        # Generar historial de pedido
        HistorialEstadoPedido.objects.create(pedido = pedido, estado = pedido.estado, fecha = pedido.actualizacion)

        # Descontar productos del inventario
        for i in carrito:
            producto = get_object_or_404(Producto, id=i.producto.id)
            producto.stock -= i.cantidad
            producto.save()

        # Eliminar carrito
        for i in carrito:
            i.delete()
            
        messages.success(request, "Tu compra se ha procesado correctamente.", extra_tags = "Compra realizada")
        return redirect(to="index")

    return render(request, 'app/compra/compra.html', data)


# VENTAS
@login_required
def ventas(request):
    # Se obtienen todas las ventas
    ventas = Compra.objects.all()

    data = {
        'ventas' : ventas
    }

    return render(request, 'app/administracion/ventas.html', data)

@login_required
def pedidos(request):
    # Se obtienen todos los pedidos
    pedidos = Pedido.objects.all()

    data = {
        'pedidos' : pedidos,
    }

    return render(request, 'app/administracion/pedidos.html', data)

@login_required
def historial_pedido(request,id):
    # Se obtienen todos los pedidos
    registros = HistorialEstadoPedido.objects.filter(pedido=id).order_by('-fecha')
    pedido = get_object_or_404(Pedido, id=id)

    data = {
        'registros' : registros,
        'pedido' : pedido,
    }

    return render(request, 'app/administracion/historial_pedido.html', data)

def actualizar_pedido(request, id):
    # Se obtiene el pedido a actualizar
    pedido = get_object_or_404(Pedido, id=id)

    data = {
        'pedido' : pedido,
        'form' : PedidoForm(instance=pedido),
    }

    if request.method == 'POST':
        formulario = PedidoForm(request.POST, instance=pedido)
        if formulario.is_valid():
            form = formulario.save(commit=False)
            form.actualizacion = datetime.now()
            form.save()
            HistorialEstadoPedido.objects.create(pedido = pedido, estado = form.estado, fecha = form.actualizacion)
            messages.success(request, "Estado de pedido actualizado correctamente.", extra_tags="Actualizado")
            return redirect(to="pedidos")

    return render(request, 'app/administracion/actualizar_pedido.html', data)

@login_required
def clientes(request):
    # Se obtienen todos los clientes
    clientes = User.objects.all().exclude(is_superuser=True)

    data = {
        'clientes' : clientes
    }

    return render(request, 'app/administracion/clientes.html', data)

# VENTAS
@login_required
def compras(request):
    # Se obtienen todas las compras
    compras = Compra.objects.filter(comprador = request.user)

    data = {
        'compras' : compras
    }

    return render(request, 'app/cliente/compras.html', data)

@login_required
def pedidos_cliente(request):
    # Se obtienen todas las compras del cliente
    compras_usuario = Compra.objects.filter(comprador = request.user)

    # Se obtienen pedidos segun compras del cliente
    pedidos = []
    for i in compras_usuario:
        pedidos.append(Pedido.objects.get(compra = i))

    data = {
        'pedidos' : pedidos
    }

    return render(request, 'app/cliente/pedidos_cliente.html', data)