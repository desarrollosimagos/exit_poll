#encoding:utf-8
from django.forms import ModelForm
from django import forms
from apps.candidatos.models import Candidatos


class CandidatosForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Candidatos` """
    class Meta:
        model = Candidatos
