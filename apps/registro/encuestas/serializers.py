from rest_framework import serializers
from .models import Encuesta


class EncuestaSerializer(serializers.ModelSerializer):
    """ Clase donde llamamos al modelo `Encuesta` y serializamos los campos. """
    class Meta:
        model = Encuesta
        fields = ('id', 'cod_encuesta', 'nombre',  'estatus', 'tipo',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
