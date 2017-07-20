#encoding:utf-8
from django.forms import ModelForm
from django import forms
from apps.circuitos.models import Circuito


class CircuitoForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Circuito`."""
    class Meta:
        model = Circuito
