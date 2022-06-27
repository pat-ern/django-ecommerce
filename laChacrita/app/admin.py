from django.contrib import admin
from .models import \
    Compra, DetalleCarrito, DetalleCompra, EstadoPedido, HistorialEstadoPedido, Pedido, \
    TipoSuscripcion, CategoriaProducto, Producto, Calificacion, AsuntoContacto, Contacto, \
    TipoSuscripcion, Suscripcion

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "precio", "puntuacion_avg", "stock"]
    list_editable = ["categoria","precio", "puntuacion_avg", "stock"]
    search_fields = ["nombre"]
    list_per_page = 20
    ordering = ('-id',)

class AsuntoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "id"]
    ordering = ('id',)

class TipoSuscripcionAdmin(admin.ModelAdmin):
    list_display = ["nombre", "id", "monto"]
    ordering = ('id',)

class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha", "tipo_suscripcion", "recibe_informe", "estado"]
    ordering = ('-id',)

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "idProducto", "puntuacion", "usuario", "fecha"]
    ordering = ('-id',)

class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ["nombreCategoria", "idCategoria"]
    ordering = ('idCategoria',)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["asunto", "correo", "fecha"]
    ordering = ('-fecha',)

class DetalleCarritoAdmin(admin.ModelAdmin):
    list_display = ["producto", "cantidad", "comprador", "subtotal"]

class CompraAdmin(admin.ModelAdmin):
    list_display = ["__str__", "comprador", "fecha", "total", "descuento", "valor_final"]
    ordering = ('-fecha',)

class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ["__str__", "producto", "compra", "cantidad", "subtotal"]
    ordering = ('-id',)

class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ["descripcion", "id"]
    ordering = ('id',)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "compra", "estado"]

class HistorialEstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "pedido", "estado", "fecha"]
    ordering = ('-fecha',)

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(AsuntoContacto, AsuntoAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(TipoSuscripcion, TipoSuscripcionAdmin)
admin.site.register(Suscripcion, SuscripcionAdmin)
admin.site.register(DetalleCarrito, DetalleCarritoAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(DetalleCompra, DetalleCompraAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(EstadoPedido, EstadoPedidoAdmin)
admin.site.register(HistorialEstadoPedido, HistorialEstadoPedidoAdmin)