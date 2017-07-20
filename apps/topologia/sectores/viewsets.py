from .models import Sector
from .serializers import SectorSerializer
from rest_framework import serializers, viewsets


class SectorViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los serializers
    """
    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
