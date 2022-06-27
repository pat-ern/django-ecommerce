from rest_framework import serializers
from app.models import Suscripcion

class SuscripcionSerializer(serializers.ModelSerializer):
    
    suscriptor_nombre = serializers.CharField(read_only = True, source = 'suscriptor.username')

    class Meta:
        model = Suscripcion
        fields = "__all__"