from django.urls import path
from . import views
from .views import \
    eliminar_calificacion, producto, conocenos, contacto, agregarProducto, lista_productos, modificarProducto, eliminarProducto, \
    estado_suscripcion, lista_suscripciones, crear_suscripcion, cancelar_suscripcion, modificar_suscripcion, \
    inicio_sesion, registro_usuario, carrito_compras, eliminar_de_carrito

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

    path('iniciosesion/', inicio_sesion, name="inicio_sesion"),
    path('registro/', registro_usuario, name="registro_usuario"), 

    path('carrito/', carrito_compras, name='carrito'),
    path('eliminardecarrito/<id>/', eliminar_de_carrito, name='eliminar_de_carrito'),

    path('eliminarcalificacion/<id>/', eliminar_calificacion, name="eliminar_calificacion"), 
]