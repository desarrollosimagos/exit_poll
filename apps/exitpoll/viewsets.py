from .models import ExitPoll
from .serializers import ExitPollSerializer
from rest_framework import serializers, viewsets


class ExitPollViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los `serializers`.
    """
    serializer_class = ExitPollSerializer
    queryset = ExitPoll.objects.all()

