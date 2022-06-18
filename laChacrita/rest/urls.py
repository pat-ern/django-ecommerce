from django.urls import path
from rest.views import lista_suscripcion, detalle_suscripcion
from rest.viewslogin import login

urlpatterns = [
    path('lista_suscripcion', lista_suscripcion, name = 'lista_suscripcion'),
    path('detalle_suscripcion/<id>', detalle_suscripcion, name = 'detalle_suscripcion'),
    path('login', login, name = 'login'),
]