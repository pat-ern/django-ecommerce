from django.contrib import admin
from .models import CategoriaProducto, Usuario, Producto, Calificacion, CompraProducto, AsuntoContacto, Contacto, TipoDonacion, Donacion, FiltroPrecios

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["categoria"]
    list_per_page = 10

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "asunto"]
    list_filter = ["asunto"]

class TipoDonacionAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(CategoriaProducto)
admin.site.register(Usuario)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Calificacion)
admin.site.register(CompraProducto)
admin.site.register(AsuntoContacto)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(TipoDonacion, TipoDonacionAdmin)
admin.site.register(Donacion)
admin.site.register(FiltroPrecios)