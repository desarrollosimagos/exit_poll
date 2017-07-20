from .models import Candidatos
from .serializers import CandidatosSerializer
from rest_framework import serializers, viewsets


class CandidatosViewSet(viewsets.ModelViewSet):
    """ Clase que construye la vista de los `serializers`."""
    serializer_class = CandidatosSerializer
    queryset = Candidatos.objects.all()
