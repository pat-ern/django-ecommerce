from django.urls import path
from rest.views import lista_productos, detalle_producto

urlpatterns = [
    path('lista_productos', lista_productos, name = 'lista_productos'),
    path('detalle_producto/<nombre>', detalle_producto, name = 'detalle_producto'),
]