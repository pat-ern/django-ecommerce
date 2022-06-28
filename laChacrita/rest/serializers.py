from rest_framework import serializers
from app.models import Suscripcion

class SuscripcionSerializer(serializers.ModelSerializer):
    
    suscriptor_nombre = serializers.CharField(read_only = True, source = 'suscriptor.username')
    suscripcion_nombre = serializers.CharField(read_only = True, source = 'tipo_suscripcion.nombre')
    suscripcion_cuota = serializers.CharField(read_only = True, source = 'tipo_suscripcion.monto')
    suscripcion_desc = serializers.CharField(read_only = True, source = 'tipo_suscripcion.desc')

    class Meta:
        model = Suscripcion
        fields = "__all__"