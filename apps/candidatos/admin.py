# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.candidatos.models import Candidatos


class CandidatosAdmin(admin.ModelAdmin):
    """
    :param fieldsets: se organiza interfaz CandidatosAdmin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
        ('Información Principal', {'fields': ['nombre', 'apellido', 'cedula', 'sexo', 'edad', 'foto', 'twitter', 'part_politico', 'candidato_activo']}),
        ('Auditoria', {'fields': ['user_create', 'user_update']})]
    list_display = ('cedula', 'nombre', 'apellido', 'sexo', 'twitter')
    list_filter = ['part_politico']
    search_fields = ['cedula', 'nombre', 'apellido']

admin.site.register(Candidatos, CandidatosAdmin)
