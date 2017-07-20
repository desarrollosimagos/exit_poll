from rest_framework import serializers
from .models import Eleccion


class EleccionSerializer(serializers.ModelSerializer):
    """
        Clase donde llamamos al modelo `Eleccion` y serializamos los campos
    """
    class Meta:
        model = Eleccion
        fields = ('id', 'nombre', 'tipo_eleccion', 'categoria_eleccion', 'ele_activa',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update',)
