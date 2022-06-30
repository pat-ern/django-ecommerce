import random
from app.models import DetalleCarrito, Promocion, TipoSuscripcion

def cart_processor(request):
    cant = 0
    if request.user.is_authenticated:
        carrito = DetalleCarrito.objects.filter(comprador = request.user)
        for i in carrito:
            cant += i.cantidad
    return {'items_carrito': cant}

def tipo_subs_processor(request):
    tipo_subs = TipoSuscripcion.objects.all()
    return {'tipo_subs': tipo_subs}

def promociones_processor(request):
    promociones = Promocion.objects.exclude(nombre = 'sin promocion')
    random_promo = random.choice(promociones)
    return {'promo': random_promo}