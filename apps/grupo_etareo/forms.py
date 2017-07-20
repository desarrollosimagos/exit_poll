#encoding:utf-8
from django.forms import ModelForm
from django import forms
from apps.grupo_etareo.models import Grupo_Etareo


class Grupo_EtareoForm(forms.ModelForm):
    """
    Clase de donde se define la estructura del formulario `Grupo_Etareo`
    """
    class Meta:
        model = Grupo_Etareo

