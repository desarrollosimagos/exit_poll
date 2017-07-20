from rest_framework import serializers
from .models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    """ Clase donde llamamos al modelo `Categoria` y serializamos los campos"""
    class Meta:
        model = Categoria
        fields = ('id', 'categoria', 'user_create', 'user_update', 'fecha_create', 'fecha_update',)
