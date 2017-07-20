from django.contrib import admin
from .models import Poligonal


class PoligonalAdmin(admin.ModelAdmin):
    """

    :param fieldsets: se organiza interfaz CandidatosAdmin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
            ('Informacion Principal', {'fields': ['cod_pol', 'poligonal']}),
            ('Ubicacion', {'fields': ['estado',  'municipio', 'parroquia', 'sector']}),
            ('Auditoria', {'fields': ['user_create', 'user_update']})]

    list_display = ('cod_pol', 'poligonal', 'estado', 'municipio', 'parroquia')
    list_filter = ['estado']
    search_fields = ['cod_pol', 'poligonal']

admin.site.register(Poligonal, PoligonalAdmin)
