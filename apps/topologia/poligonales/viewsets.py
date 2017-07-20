from .models import Poligonal
from .serializers import PoligonalSerializer
from rest_framework import serializers, viewsets


class PoligonalViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los serializers
    """
    serializer_class = PoligonalSerializer
    queryset = Poligonal.objects.all()
