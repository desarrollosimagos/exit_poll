from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.elecciones.models import Eleccion
from apps.registro.encuestas.models import Encuesta
from django.db import connection, transaction


class Inicio(TemplateView):
    """ Vista basada en clase: (`Plantilla`)
    :param template_name: ruta al archivo que contiene la plantilla principal de la aplicacion
    """
    template_name = 'inicio.html'

    
class PrincipalEncuesta(TemplateView):
    """ Vista basada en clase: (`Plantilla`)
    :param template_name: ruta al archivo que contiene la plantilla principal de la aplicacion
    """
    template_name = 'principal_encuesta.html'
    
    def get_context_data(self, **kwargs):
        context = super(PrincipalEncuesta, self).get_context_data(**kwargs)
        usuario_id = self.request.user.id
        encuestas = Encuesta.objects.all()

        # Captura del ID del Grupo 'Web'
        cursor = connection.cursor()
        sql_gru = "SELECT id FROM auth_group WHERE name = 'Web'"
        cursor.execute(sql_gru)
        row = dictfetchall(cursor)
        if row == []:
            id_grupo = 0
        else:
            id_grupo = row[0]['id']

        # Consulta a la tabla user_group si el usuario pertenece al grupo 'Web'
        cursor = connection.cursor()
        sql_use = "SELECT id FROM auth_user_groups"
        sql_use += " WHERE user_id=%s and group_id =%s;"
        cursor.execute(sql_use, [usuario_id, id_grupo])
        row2 = dictfetchall(cursor)
        if row2 == []:
            listar = encuestas
        else:
            listar = encuestas.filter(user_create_id=usuario_id)

        context['list_e'] = listar
        return context


class PrincipalExit(TemplateView):
    """ Vista basada en clase: (`Plantilla`)
    :param template_name: ruta al archivo que contiene la plantilla principal de la aplicacion
    """
    template_name = 'principal_exit_poll.html'

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(PrincipalExit, self).get_context_data(**kwargs)
        # Agregamos un QuerySet
        context['list_t'] = Eleccion.objects.all()
        return context

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]