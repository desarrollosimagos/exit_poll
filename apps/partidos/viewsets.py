from .models import Partidos
from .serializers import PartidosSerializer
from rest_framework import serializers, viewsets


class PartidosViewSet(viewsets.ModelViewSet):
    """ Clase que construye la vista de los `serializers`. """
    serializer_class = PartidosSerializer
    queryset = Partidos.objects.all()
