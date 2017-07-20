from .models import Respuestas
from .serializers import RespuestasSerializer
from rest_framework import serializers, viewsets


class RespuestasViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los serializers
    """
    serializer_class = RespuestasSerializer
    queryset = Respuestas.objects.all()
