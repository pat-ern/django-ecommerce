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
    list_display = ["id", "nombre"]
    ordering = ('id',)

class TipoDonacionAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]
    ordering = ('id',)

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "comentario", "puntuacion"]
    ordering = ('id',)

admin.site.register(Usuario)
admin.site.register(CategoriaProducto)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(CompraProducto)
admin.site.register(AsuntoContacto, AsuntoAdmin)
admin.site.register(Contacto)
admin.site.register(TipoDonacion, TipoDonacionAdmin)
admin.site.register(Donacion)