from rest_framework import serializers
from .models import Sector


class SectorSerializer(serializers.ModelSerializer):
    """ Clase donde llamamos al modelo `Sector` y serializamos los campos. """
    class Meta:
        model = Sector
        fields = ('id', 'cod_s', 'sector', 'estado', 'municipio', 'parroquia',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
