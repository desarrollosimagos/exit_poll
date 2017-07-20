# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.tipos.categoria_eleccion.models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    """
    :param list_display: Muesta el str de los campos en la vista lista
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    :param fieldsets: se organiza interfaz CategoriaAdmin
    """
    fieldsets = [('Categorias', {'fields': ['categoria']})]
    list_display = ('categoria', 'user_create', 'user_update', 'fecha_create', 'fecha_update')
    search_fields = ['categoria']

admin.site.register(Categoria, CategoriaAdmin)
