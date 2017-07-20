from rest_framework import serializers
from .models import Circuito


class CircuitoSerializer(serializers.ModelSerializer):
    """
        Clase donde llamamos al modelo `Circuito` y serializamos los campos
    """
    class Meta:
        model = Circuito
        fields = ('id', 'estado', 'n_circuito', 'num_max_candidatos',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
