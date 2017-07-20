from rest_framework import serializers
from .models import Poligonal


class PoligonalSerializer(serializers.ModelSerializer):
    """ Clase donde llamamos al modelo `Poligonal` y serializamos los campos. """
    class Meta:
        model = Poligonal
        fields = ('id', 'cod_pol', 'poligonal', 'estado', 'municipio', 'parroquia', 'sector',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
