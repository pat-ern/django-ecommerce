from app.models import DetalleCarrito, TipoSuscripcion

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