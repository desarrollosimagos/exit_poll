from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework import serializers, viewsets


class CategoriaViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los `serializers`
    """
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
