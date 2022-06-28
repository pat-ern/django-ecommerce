from app.models import DetalleCarrito

def cart_processor(request):
    cant = 0
    # Se obtiene total de productos en el carrito de usuario
    if request.user.is_authenticated:
        carrito = DetalleCarrito.objects.filter(comprador = request.user)
        # Contar cantidad de productos en carrito
        
        for i in carrito:
            cant += i.cantidad

    return {'items_carrito': cant}