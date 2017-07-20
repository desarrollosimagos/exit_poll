from django.contrib import admin
from .models import Preguntas


class PreguntasAdmin(admin.ModelAdmin):
    """

    :param fieldsets: se organiza interfaz CandidatosAdmin
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    fieldsets = [
            ('Informacion Principal', {'fields': ['cod_pregunta', 'pregunta']}),
            ('Auditoria', {'fields': ['user_create', 'user_update']})]

    list_display = ('cod_pregunta', 'pregunta')
    list_filter = ['pregunta']
    search_fields = ['cod_pregunta', 'pregunta']

admin.site.register(Preguntas, PreguntasAdmin)
