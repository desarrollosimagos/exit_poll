from django import forms
from .models import ExitPoll


class ExitPollForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `ExitPoll` """
    class Meta:
        model = ExitPoll
