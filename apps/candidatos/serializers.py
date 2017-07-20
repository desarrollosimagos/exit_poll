from rest_framework import serializers
from .models import Candidatos, SEXO


class CandidatosSerializer(serializers.ModelSerializer):
    """ Clase donde llamamos al modelo `Candidatos` y serializamos los campos."""
    class Meta:
        model = Candidatos
        fields = ('id', 'nombre', 'apellido', 'cedula', 'foto_binario', 'sexo',
                  'edad', 'twitter', 'part_politico',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update','candidato_activo',)
