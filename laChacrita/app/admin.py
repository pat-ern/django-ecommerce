from django.contrib import admin
from .models import Usuario, CategoriaProducto, Producto, Calificacion, CompraProducto, AsuntoContacto, Contacto, TipoDonacion, Donacion

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "categoria", "precio"]
    list_editable = ["categoria","precio"]
    search_fields = ["nombre"]
    list_per_page = 20
    ordering = ('id',)

class AsuntoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "id"]
    ordering = ('id',)

class TipoDonacionAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]
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
admin.site.register(TipoDonacion, TipoDonacionAdmin)
admin.site.register(Donacion)