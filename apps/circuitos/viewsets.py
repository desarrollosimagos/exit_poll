from .models import Circuito
from .serializers import CircuitoSerializer
from rest_framework import serializers, viewsets


class CircuitoViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los `serializers`
    """
    serializer_class = CircuitoSerializer
    queryset = Circuito.objects.all()
