from django.contrib import admin
from .models import Sector


class SectorAdmin(admin.ModelAdmin):
    """

    :param fieldsets: se organiza interfaz CandidatosAdmin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
            ('Informacion Principal', {'fields': ['cod_s', 'sector']}),
            ('Ubicacion', {'fields': ['estado',  'municipio', 'parroquia' ]}),
            ('Auditoria', {'fields': ['user_create', 'user_update']})]

    list_display = ('cod_s', 'sector', 'estado', 'municipio', 'parroquia')
    list_filter = ['estado']
    search_fields = ['cod_s', 'sector']

admin.site.register(Sector, SectorAdmin)