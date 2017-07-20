#encoding:utf-8
from django.forms import ModelForm
from django import forms
from apps.elecciones.models import Eleccion


class EleccionForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Eleccion`"""
    class Meta:
        model = Eleccion
