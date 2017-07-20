#encoding:utf-8
from django.forms import ModelForm
from django import forms
from apps.partidos.models import Partidos


class PartidosForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Partidos`."""
    class Meta:
        model = Partidos
