from django.contrib import admin
from .models import CategoriaProducto, Usuario, Producto, Calificacion, CompraProducto, AsuntoContacto, Contacto, TipoDonacion, Donacion, FiltroPrecios, Snippet

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    #list_filter = [""]
    list_per_page = 20

class AsuntoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

class TipoDonacionAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(CategoriaProducto)
admin.site.register(Usuario)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Calificacion)
admin.site.register(CompraProducto)
admin.site.register(AsuntoContacto, AsuntoAdmin)
admin.site.register(Contacto)
admin.site.register(TipoDonacion, TipoDonacionAdmin)
admin.site.register(Donacion)
admin.site.register(FiltroPrecios)
admin.site.register(Snippet)