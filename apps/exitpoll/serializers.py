from rest_framework import serializers
from .models import ExitPoll


class ExitPollSerializer(serializers.ModelSerializer):
    """ Clase donde llamamos al modelo `ExitPoll` y serializamos los campos."""
    class Meta:
        model = ExitPoll
        fields = ('eleccion', 'candidatos', 'estado', 'municipio', 'parroquia', 'sector', 'poligonal', 'user_create', 'user_update', 'fecha_create', 'fecha_update',)
