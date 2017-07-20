#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Poligonal


class PoligonalForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Poligonal`."""
    class Meta:
        model = Poligonal
