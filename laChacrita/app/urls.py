from django.urls import path
from .views import estado_suscripcion, producto, conocenos, contacto, agregarProducto, lista_productos, modificarProducto, eliminarProducto
from .views import lista_suscripciones, crear_suscripcion, cancelar_suscripcion, modificar_suscripcion 
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('producto/<id>/', producto, name="producto"), 
    path('conocenos/', conocenos, name="conocenos"), 
    path('contacto/', contacto, name="contacto"), 

    path('agregar/', agregarProducto, name="agregar_producto"), 
    path('productos/', lista_productos, name="lista_productos"), 
    path('modificar/<id>/', modificarProducto, name="modificar_producto"), 
    path('eliminar/<id>/', eliminarProducto, name="eliminar_producto"), 

    path('suscribirse/', crear_suscripcion, name="suscribirse"), 
    path('suscripciones/', lista_suscripciones, name="lista_suscripciones"), 
    path('cancelarsuscripcion/<id>/', cancelar_suscripcion, name="cancelar"), 
    path('modificarsuscripcion/<id>/', modificar_suscripcion, name="modificar_suscripcion"), 
    path('cambiarestado/<id>/', estado_suscripcion, name="estado_suscripcion"), 
]