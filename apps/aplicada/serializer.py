from rest_framework import serializers
from apps.registro.respuestas.models import Respuestas
from apps.registro.preguntas.serializers import PreguntasSerializer


class AplicadaSerializer(serializers.ModelSerializer):
    """ Clase donde llamamos al modelo `Respuestas` y serializamos los campos. """

    cod_pregunta_id = PreguntasSerializer(many=False, read_only=True)

    class Meta:
        model = Respuestas
        fields = ('id', 'cod_pregunta_id', 'cod_respuesta',  'respuesta', 'tipo')
