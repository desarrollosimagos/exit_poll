from rest_framework import serializers
from .models import Preguntas


class PreguntasSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Preguntas
        fields = ('id', 'cod_encuesta', 'cod_pregunta', 'pregunta',  'tipo')
