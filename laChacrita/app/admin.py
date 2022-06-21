from django.contrib import admin
from .models import TipoSuscripcion, Usuario, CategoriaProducto, Producto, Calificacion, CompraProducto, AsuntoContacto, Contacto, TipoSuscripcion, Suscripcion

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "precio", "puntuacion_avg"]
    list_editable = ["categoria","precio", "puntuacion_avg"]
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
    list_display = ["id", "nombre", "correo", "fecha", "telefono", "tipo_suscripcion", "recibe_informe", "estado"]
    ordering = ('id',)

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ["comentario", "idProducto", "usuario", "puntuacion"]
    ordering = ('-id',)

class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ["nombreCategoria", "idCategoria"]
    ordering = ('idCategoria',)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["asunto", "correo", "fecha"]
    ordering = ('-fecha',)

admin.site.register(Usuario)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(CompraProducto)
admin.site.register(AsuntoContacto, AsuntoAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(TipoSuscripcion, TipoSuscripcionAdmin)
admin.site.register(Suscripcion, SuscripcionAdmin)