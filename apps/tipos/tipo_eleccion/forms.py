#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Tipo_eleccion


class Tipo_eleccionForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Tipo_eleccion`."""
    class Meta:
        model = Tipo_eleccion
