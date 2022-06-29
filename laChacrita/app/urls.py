from django.urls import path
from . import views
from .views import \
    actualizar_pedido, cambiar_suscripcion, clientes, compra, compras, desuscribirse, eliminar_calificacion, historial_pedido, pedidos, pedidos_cliente, producto, conocenos, contacto, agregarProducto, lista_productos, modificarProducto, eliminarProducto, \
    estado_suscripcion, lista_suscripciones, crear_suscripcion, cancelar_suscripcion, modificar_suscripcion, \
    inicio_sesion, registro_usuario, carrito_compras, eliminar_de_carrito, suscripcion, ventas

urlpatterns = [
    # PRODUCTOS Y DETALLE PRODUCTO
    path('', views.Index.as_view(), name='index'),
    path('producto/<id>/', producto, name="producto"), 
    path('eliminarcalificacion/<id>/', eliminar_calificacion, name="eliminar_calificacion"), 
    # CRUD PRODUCTOS
    path('agregar/', agregarProducto, name="agregar_producto"), 
    path('productos/', lista_productos, name="lista_productos"), 
    path('modificar/<id>/', modificarProducto, name="modificar_producto"), 
    path('eliminar/<id>/', eliminarProducto, name="eliminar_producto"), 
    # CRUD SUSCRIPCIONES CLIENTE
    path('suscripcion/', suscripcion, name="suscripcion"), 
    path('cambiarsuscripcion/<id>/', cambiar_suscripcion, name="cambiar_suscripcion"), 
    path('desuscribirse/<id>/', desuscribirse, name="desuscribirse"), 
    # CRUD SUSCRIPCIONES ADMIN
    path('suscripciones/', lista_suscripciones, name="lista_suscripciones"), 
    path('crearsuscripcion/', crear_suscripcion, name="crear_suscripcion"), 
    path('cancelarsuscripcion/<id>/', cancelar_suscripcion, name="cancelar"), 
    path('modificarsuscripcion/<id>/', modificar_suscripcion, name="modificar_suscripcion"), 
    path('cambiarestado/<id>/', estado_suscripcion, name="estado_suscripcion"), 
    # LOGIN Y REGISTRO
    path('iniciosesion/', inicio_sesion, name="inicio_sesion"),
    path('registro/', registro_usuario, name="registro_usuario"), 
    # PROCESO DE COMPRA CLIENTE
    path('carrito/', carrito_compras, name='carrito'),
    path('eliminardecarrito/<id>/', eliminar_de_carrito, name='eliminar_de_carrito'),
    path('detallecompra/', compra, name="detalle_compra"), 
    path('compras/', compras, name="compras"),  
    path('pedidos_cliente/', pedidos_cliente, name="pedidos_cliente"),  
    # ADMINISTRACION DE VENTAS Y PEDIDOS
    path('ventas/', ventas, name="ventas"), 
    path('pedidos/', pedidos, name="pedidos"), 
    path('actualizarpedido/<id>', actualizar_pedido, name="actualizarpedido"),
    path('historial_pedido/<id>', historial_pedido, name="historial_pedido"),
    path('clientes/', clientes, name="clientes"),  
    # OTROS
    path('conocenos/', conocenos, name="conocenos"), 
    path('contacto/', contacto, name="contacto"), 
]