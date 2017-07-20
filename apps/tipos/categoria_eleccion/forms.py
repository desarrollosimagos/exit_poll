#encoding:utf-8
from django.forms import ModelForm
from django import forms
from apps.tipos.categoria_eleccion.models import Categoria


class CategoriaForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Categoria`."""
    class Meta:
        model = Categoria
