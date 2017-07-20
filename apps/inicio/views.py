from django.shortcuts import render
from django.views.generic import TemplateView


class Inicio(TemplateView):
    """ Vista basada en clase: (`Plantilla`)

    :param template_name: ruta al archivo que contiene la plantilla
    """
    template_name = 'inicio.html'
