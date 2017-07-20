# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Partidos


class PartidosAdmin(admin.ModelAdmin):
    """ Clase Administrador para todo lo referente a los Partidos: (Registrar, Modificar, Eliminar y Consultar)

    :param fieldsets: se organiza la vista de Creación y Edición en la interfaz Admin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """

    fieldsets = [
        ('Informacion Principal', {'fields': ['n_partidos', 'siglas', 'foto_partido']}),
        ('Responsable ', {'fields': ['nom_presidente', 'ape_presidente']}),
        ('Contacto', {'fields': ['correo',  'twitter', 'telefono']}),
        ('Auditoria', {'fields': ['user_create', 'user_update']})]

    list_display = ('siglas', 'n_partidos', 'telefono', 'correo', 'twitter')
    list_filter = ['siglas']
    search_fields = ['siglas', 'n_partidos']

admin.site.register(Partidos, PartidosAdmin)
