from rest_framework import serializers
from .models import Partidos


class PartidosSerializer(serializers.ModelSerializer):
    """
        Clase donde llamamos al modelo `Partidos` y serializamos los campos
    """
    class Meta:
        model = Partidos
        fields = ('id', 'n_partidos','siglas','foto_partido','nom_presidente',
                  'ape_presidente', 'correo','twitter','telefono','partido_binario',
                  'user_create','user_update','fecha_create','fecha_update',)
