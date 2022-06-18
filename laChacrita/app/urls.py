from django.urls import path
from .views import producto, conocenos, contacto, agregarProducto, listarProducto, modificarProducto, eliminarProducto, listar_suscripciones, crear_suscripcion, cancelar_suscripcion, modificar_suscripcion 
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('producto/<id>/', producto, name="producto"), 
    path('conocenos/', conocenos, name="conocenos"), 
    path('contacto/', contacto, name="contacto"), 
    path('agregar/', agregarProducto, name="agregar_producto"), 
    path('listar/', listarProducto, name="listar_producto"), 
    path('modificar/<id>/', modificarProducto, name="modificar_producto"), 
    path('eliminar/<id>/', eliminarProducto, name="eliminar_producto"), 
    path('suscripciones/', listar_suscripciones, name="suscripciones"), 
    path('suscripcion/', crear_suscripcion, name="suscripcion"), 
    path('cancelarsuscripcion/<id>/', cancelar_suscripcion, name="cancelar"), 
    path('modificarsuscripcion/<id>/', modificar_suscripcion, name="modificar_suscripcion"), 
]