# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.tipos.tipo_eleccion.models import Tipo_eleccion


class TipoAdmin(admin.ModelAdmin):
    """
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    list_display = ('tipo', 'categoria')
    list_filter = ['categoria', ]
    search_fields = ['categoria', 'tipo']

admin.site.register(Tipo_eleccion, TipoAdmin)
