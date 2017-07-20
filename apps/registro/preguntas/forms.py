#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Preguntas


class PreguntasForm(forms.ModelForm):
    """
    Clase de donde se define la estructura del formulario `Preguntas`
    """
    class Meta:
        model = Preguntas

