from django.contrib import admin
from .models import CategoriaProducto, Usuario, Producto, Calificacion, CompraProducto, AsuntoContacto, Contacto, TipoDonacion, Donacion

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    #list_filter = [""]
    list_per_page = 20

admin.site.register(CategoriaProducto)
admin.site.register(Usuario)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Calificacion)
admin.site.register(CompraProducto)
admin.site.register(AsuntoContacto)
admin.site.register(Contacto)
admin.site.register(TipoDonacion)
admin.site.register(Donacion)