# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Eleccion


class EleccionAdmin(admin.ModelAdmin):
    """
    :param fieldsets: se organiza interfaz CandidatosAdmin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
        ('Informacion Principal', {'fields': ['nombre', 'categoria_eleccion', 'tipo_eleccion', 'ele_activa']}),
        ('Auditoria', {'fields': ['user_create', 'user_update', ]}),
                ]

    list_display = ['nombre', 'categoria_eleccion', 'tipo_eleccion']
    list_filter = ['categoria_eleccion', 'tipo_eleccion']
    search_fields = ['nombre', 'tipo_eleccion', 'tipo_candidatura']

admin.site.register(Eleccion, EleccionAdmin)
