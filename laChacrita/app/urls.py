from django.urls import path
from .views import index, producto, conocenos, contacto, donaciones, agregarProducto, modificarProducto
from . import views

urlpatterns = [
    path('', index, name = "index"),
    path('producto/<id>/', producto, name="producto"), 
    path('conocenos/', conocenos, name="conocenos"), 
    path('contacto/', contacto, name="contacto"), 
    path('donaciones/', donaciones, name="donaciones"), 
    path('agregar/', agregarProducto, name="agregar_producto"), 
    path('modificar/', modificarProducto, name="modificar_producto"), 
    path('snippet', views.SnippetListView.as_view(), name='list'),
    path('snippet/<int:pk>/', views.SnippetDetailView.as_view(), name='detail')
]