# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.exitpoll.models import ExitPoll


#Configuracion del Modelo Exitpoll en la vista Administrador (vista,filtros,busqueda)
class ExitPollAdmin(admin.ModelAdmin):
    """
    :param fieldsets: se organiza interfaz ExitPollAdmin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
        ('ExitPoll', {'fields': ['eleccion','candidatos', 'estado', 'municipio', 'parroquia', 'circuito' ]}),
        ('Auditoria', {'fields': ['user_create', 'user_update', ]}),
        ]
    list_display = ('eleccion','candidatos', 'fecha_create') #Muesta el str de los campos en la vista lista
    list_filter = ['eleccion','candidatos'] #Crea un fitro y definimos en base a cuales campos filtrara
    search_fields = ['eleccion','candidatos'] #Crea un fitro y definimos en base a cuales campos filtrara

admin.site.register(ExitPoll, ExitPollAdmin)



