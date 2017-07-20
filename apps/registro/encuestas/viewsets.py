from .models import Encuesta
from .serializers import EncuestaSerializer
from rest_framework import serializers, viewsets


class EncuestaViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los serializers
    """
    serializer_class = EncuestaSerializer
    queryset = Encuesta.objects.all()
