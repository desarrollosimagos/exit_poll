from .models import Eleccion
from .serializers import EleccionSerializer
from rest_framework import serializers, viewsets


class EleccionViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los `serializers`
    """
    serializer_class = EleccionSerializer
    queryset = Eleccion.objects.all()
