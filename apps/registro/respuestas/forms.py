#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Respuestas


class RespuestasForm(forms.ModelForm):
    """
    Clase de donde se define la estructura del formulario `Respuestas`
    """
    class Meta:
        model = Respuestas

