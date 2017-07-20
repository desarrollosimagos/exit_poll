from .models import Preguntas
from .serializers import PreguntasSerializer
from rest_framework import serializers, viewsets


class PreguntasViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los serializers
    """
    serializer_class = PreguntasSerializer
    queryset = Preguntas.objects.all()
