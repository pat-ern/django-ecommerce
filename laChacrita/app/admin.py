from django.contrib import admin
from .models import Usuario, CategoriaProducto, Producto, Calificacion, CompraProducto, AsuntoContacto, Contacto, TipoDonacion, Donacion

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "categoria", "precio"]
    list_editable = ["categoria","precio"]
    search_fields = ["nombre"]
    list_filter = ["categoria"]
    list_per_page = 10
    ordering = ('id',)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "asunto"]
    list_filter = ["asunto"]
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
admin.site.register(AsuntoContacto)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(TipoDonacion, TipoDonacionAdmin)
admin.site.register(Donacion)