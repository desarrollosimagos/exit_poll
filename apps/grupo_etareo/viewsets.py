from .models import Grupo_Etareo
from .serializers import Grupo_EtareoSerializer
from rest_framework import serializers, viewsets


class Grupo_EtareoViewSet(viewsets.ModelViewSet):
    """ Clase que construye la vista de los `serializers` """
    serializer_class = Grupo_EtareoSerializer
    queryset = Grupo_Etareo.objects.all()
