#encoding:utf-8
from django.views.generic import CreateView, TemplateView, DetailView, ListView, View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from apps.registro.encuestas.models import Encuesta
from django.core import serializers
from django.db.models import Count
import json
import sys
from django.http import HttpResponse
from django.template import RequestContext
from django.db import connection, transaction
import time
from apps.reportes.reportes_encuestas.formato_reportes import reporte_encuesta
from django.conf import settings


class FiltroEncuestas(TemplateView):

    #model = Votacion
    template_name = 'reportes/encuestas/reporte_encuestas.html'

    def get_context_data(self, **kwargs):
        context = super(FiltroEncuestas, self).get_context_data(**kwargs)
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
            listar = encuestas.filter(estatus__in=[2,3])
        else:
            listar = encuestas.filter(estatus__in=[2,3], user_create_id=usuario_id)

        context['listar'] = listar
        return context
    
    def post(self, request, *args, **kwargs):

        id_enc = self.request.POST.get('id_encuesta')
        response_data = []
        context = super(FiltroEncuestas, self).get_context_data(**kwargs)
        cursor = connection.cursor()

        sql_res = " SELECT id "
        sql_res += " FROM preguntas_preguntas WHERE cod_encuesta= %s"
        cursor.execute(sql_res, [id_enc])

        row = dictfetchall(cursor)
        if row != []:
            sql_to = " SELECT "
            sql_to += " DISTINCT  "
            sql_to += " p.id, p.pregunta AS preguntas, "
            sql_to += " array_to_string(array_agg(r.respuesta || '//' || "
            sql_to += " (SELECT COUNT(cod_respuesta) FROM aplicada_encuestaresultado where cod_respuesta=r.id )),'@@') AS respuestas, "
            sql_to += " array_to_string(array_agg((SELECT COUNT(cod_respuesta) FROM aplicada_encuestaresultado where cod_respuesta=r.id )),'::') as total "
            sql_to += " FROM respuestas_respuestas as r "
            sql_to += " inner join preguntas_preguntas as p on r.cod_pregunta_id=p.id "
            sql_to += " inner join encuestas_encuesta as e on p.cod_encuesta=e.id "
            sql_to += " WHERE e.id = %s "
            sql_to += " group by p.pregunta, p.id"
            sql_to += " order by p.id"

            cursor.execute(sql_to, [id_enc])
            queryset = dictfetchall(cursor)
            todas = ''
            for i in queryset:
                todas += i['preguntas']+' ###'+i['respuestas']+'$$$'+i['total']+';;'
        else:
            todas = "vacio"

        return HttpResponse(todas, content_type='application/text')


class ReporteEncuesta(TemplateView):

    template_name = 'reportes/reporte_encuesta.html'
    model = Encuesta

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        sys.setdefaultencoding("utf-8")
         
        id_enc = kwargs.get('id', None)
        cursor = connection.cursor()
        sql_det = "SELECT id, cod_encuesta, nombre, estatus, fecha_create, fecha_update "
        sql_det += " FROM encuestas_encuesta "
        sql_det += " WHERE id = %s "
        cursor.execute(sql_det, [id_enc])
        row = dictfetchall(cursor)
        
        if len(row) == 0:
            response = "<body>"
            response += "<link rel='stylesheet' type='text/css' href='/static/css/bootstrap.css'>"
            response += "<script src='/static/js/bootstrap.min.js'></script>"
            response += "<img src='/static/img/disculpe.jpg' style='width:80%;margin-left:10%'/>"
            response += "<button title='Cerrar ventana' class='btn btn-danger' style='font-size:24px; width:20%; height: 10%; font-weight: bold; text-align: center;margin-left:40%' onclick=window.close()>Cerrar</button>"
            response += "<body>"
            return HttpResponse(response)
        else:
            
            nombre, archivo = reporte_encuesta.reporte_encuesta(id_enc)
            response = HttpResponse(archivo.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="'+str(nombre)
    
            return response

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
