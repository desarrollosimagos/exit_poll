from rest_framework import serializers
from .models import Respuestas
from apps.registro.preguntas.serializers import PreguntasSerializer


class RespuestasSerializer(serializers.ModelSerializer):
    """ Clase donde llamamos al modelo `Respuestas` y serializamos los campos. """
    
    cod_pregunta = PreguntasSerializer(many=False, read_only=True)
    
    class Meta:
        model = Respuestas
        fields = ('id', 'cod_pregunta', 'cod_respuesta',  'respuesta', 'tipo')

