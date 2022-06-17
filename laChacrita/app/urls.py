from django.urls import path
from .views import producto, conocenos, contacto, donaciones, agregarProducto, listarProducto, modificarProducto, eliminarProducto, suscripciones
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('producto/<id>/', producto, name="producto"), 
    path('conocenos/', conocenos, name="conocenos"), 
    path('contacto/', contacto, name="contacto"), 
    path('donaciones/', donaciones, name="donaciones"), 
    path('agregar/', agregarProducto, name="agregar_producto"), 
    path('listar/', listarProducto, name="listar_producto"), 
    path('modificar/<id>/', modificarProducto, name="modificar_producto"), 
    path('eliminar/<id>/', eliminarProducto, name="eliminar_producto"), 
    path('suscripciones/', suscripciones, name="suscripciones"), 

]