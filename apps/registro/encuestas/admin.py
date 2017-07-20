from django.contrib import admin
from .models import Encuesta


class EncuestaAdmin(admin.ModelAdmin):
    """

    :param fieldsets: se organiza interfaz CandidatosAdmin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
            ('Informacion Principal', {'fields': ['cod_encuesta', 'nombre']}),
            ('Ubicacion', {'fields': ['poblacion',  'institucion', 'nombre_c', 'apellido_c', 'cedula', 'encuesta_activa']}),
            ('Auditoria', {'fields': ['user_create', 'user_update']})]

    list_display = ('cod_encuesta', 'nombre')
    list_filter = ['nombre']
    search_fields = ['cod_encuesta', 'nombre']

admin.site.register(Encuesta, EncuestaAdmin)
