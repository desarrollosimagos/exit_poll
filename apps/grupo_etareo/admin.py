from django.contrib import admin
from apps.grupo_etareo.models import Grupo_Etareo


class Grupo_EtareoAdmin(admin.ModelAdmin):
    """ Clase Administrador para todo lo referente a los `Grupo_Etareo`: Registrar, Modificar, Eliminar y Consultar

    :param fieldsets: se organiza la vista de Creacion y Edicion en la interfaz Admin
    :param list_display: Muesta el str de los campos en la vista lista
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
        ('Grupos', {'fields': ['descripcion','desde', 'hasta']})]

    list_display = ('descripcion', 'desde', 'hasta', 'user_create', 'user_update', 'fecha_create', 'fecha_update')
    search_fields = ['grupo_etareo', ]

admin.site.register(Grupo_Etareo, Grupo_EtareoAdmin)
