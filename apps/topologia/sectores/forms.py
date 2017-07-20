#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Sector


class SectorForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Sector`."""
    class Meta:
        model = Sector
