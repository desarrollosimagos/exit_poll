# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Circuito


class CircuitosAdmin(admin.ModelAdmin):
    """
    :param fieldsets: se organiza interfaz CircuitosAdmin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
        ('Informacion Principal', {'fields': ['estado', 'n_circuito', 'num_max_candidatos']}),
        ('Auditoria', {'fields': ['user_create', 'user_update']})]
    list_display = ('estado', 'n_circuito', 'num_max_candidatos', 'fecha_create', 'fecha_update')
    list_filter = ['estado']
    search_fields = ['estado', 'n_circuito']

admin.site.register(Circuito, CircuitosAdmin)
