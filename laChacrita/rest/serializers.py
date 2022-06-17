from rest_framework import serializers
from app.models import Producto, Suscripcion

class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = "__all__"

class SuscripcionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Suscripcion
        fields = "__all__"
        