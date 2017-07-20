#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Encuesta


class EncuestaForm(forms.ModelForm):
    """
    Clase de donde se define la estructura del formulario `Encuesta`
    """
    class Meta:
        model = Encuesta

