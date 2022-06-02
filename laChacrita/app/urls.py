from django.urls import path
from .views import index, producto, conocenos, contacto, donaciones

urlpatterns = [
    path('', index, name="index"),
    path('producto/<id>/', producto, name="producto"), 
    path('conocenos/', conocenos, name="conocenos"), 
    path('contacto/', contacto, name="contacto"), 
    path('donaciones/', donaciones, name="donaciones"), 
]