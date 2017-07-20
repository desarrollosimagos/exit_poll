#encoding:utf-8
from django.views.generic import CreateView, TemplateView, DetailView, ListView, View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from apps.votacion.models import Votacion
from apps.candidatos.models import Candidatos
from apps.exitpoll.models import ExitPoll
from apps.elecciones.models import Eleccion
from apps.grupo_etareo.models import Grupo_Etareo
from apps.topologia.estados.models import Estado
from django.core import serializers
from django.db.models import Count
import json
import sys
from django.http import HttpResponse
from django.template import RequestContext
import class_pdf
from django.db import connection, transaction
import time
from apps.reportes.grafico_candidato.formato_reportes import reporte_candidato_detallado
from django.conf import settings


class GraficaCandidato(TemplateView):

    #model = Votacion
    template_name = 'reportes/grafica_candidato.html'

    def get_context_data(self, **kwargs):
        context = super(GraficaCandidato, self).get_context_data(**kwargs)

        listar_e = Eleccion.objects.all()
        listar_c = Candidatos.objects.all()
        list_estados = Estado.objects.all()
        
        context['list_estados'] = list_estados

        context['listar_e'] = listar_e
        return context

    def post(self, request, *args, **kwargs):
        id_ele = self.request.POST.get('id_eleccion')
        id_candi = self.request.POST.get('id_candidato')
        response_data = []
        context = super(GraficaCandidato, self).get_context_data(**kwargs)
        bandera = request.POST.get('bandera')
        tipo = request.POST.get('tipo')
        estado = request.POST.get('estado')
        municipio = request.POST.get('municipio')
        circuito = request.POST.get('circuito')

        if bandera == 'grupo':
            cursor = connection.cursor()
            sql_grupo = " SELECT CONCAT (g.descripcion,' (',g.desde,'-',g.hasta,' Años)') descripcion, "
            if tipo == '1':
                sql_grupo += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s AND candidatos_id=%s AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total "
            elif tipo == '2':
                sql_grupo += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s AND candidatos_id=%s AND estado="+str(estado)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total "
            elif tipo == '3':
                sql_grupo += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s AND candidatos_id=%s AND circuito="+str(circuito)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total "
            else:
                sql_grupo += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s AND candidatos_id=%s AND municipio="+str(municipio)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total "
            sql_grupo += " FROM grupo_etareo_grupo_etareo AS g ORDER BY total DESC "
            cursor.execute(sql_grupo, [id_ele, id_candi])

            queryset = dictfetchall(cursor)

        elif bandera == 'sexo':
            cursor = connection.cursor()
            sql_sexo = "SELECT sexo, COUNT(sexo) total FROM votacion_votacion "
            if tipo == '1':
                sql_sexo += " WHERE eleccion_id=%s and candidatos_id=%s "
            elif tipo == '2':
                sql_sexo += " WHERE eleccion_id=%s and candidatos_id=%s AND estado="+str(estado)+" "
            elif tipo == '3':
                sql_sexo += " WHERE eleccion_id=%s and candidatos_id=%s AND circuito="+str(circuito)+" "
            else:
                sql_sexo += " WHERE eleccion_id=%s and candidatos_id=%s AND municipio="+str(municipio)+" "
            sql_sexo += " GROUP BY sexo"
            cursor.execute(sql_sexo, [id_ele, id_candi])
            queryset = dictfetchall(cursor)

        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1

        data = json.dumps(response_data)

        return HttpResponse(data, content_type='application/json')


class ReporteCandidatoGrupo(View):

    template_name = 'reportes/grafica_candidato.html'
    model = Votacion

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        sys.setdefaultencoding("utf-8")
        eleccion = self.request.GET.get('eleccion')
        candidato = self.request.GET.get('candidato')
        tipo = self.request.GET.get('tipo')
        estado = self.request.GET.get('estado')
        circuito = self.request.GET.get('circuito')
        municipio = self.request.GET.get('municipio')

        cursor = connection.cursor()
        
        if tipo == '1':
            cursor.execute("SELECT v.grupo_etareo FROM votacion_votacion v WHERE candidatos_id="+str(candidato)+"AND eleccion_id="+str(eleccion)+"")
        elif tipo == '2':
            cursor.execute("SELECT id from votacion_votacion WHERE candidatos_id="+str(candidato)+"AND eleccion_id="+str(eleccion)+" AND estado="+str(estado)+" ")
        elif tipo == '3':
            cursor.execute("SELECT id from votacion_votacion WHERE candidatos_id="+str(candidato)+"AND eleccion_id="+str(eleccion)+" AND circuito="+str(circuito)+" ")
        else:
            cursor.execute("SELECT id from votacion_votacion WHERE candidatos_id="+str(candidato)+"AND eleccion_id="+str(eleccion)+" AND municipio="+str(municipio)+" ")

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
            nombre, archivo = reporte_candidato_detallado.reporte_candidato_detallado(eleccion,candidato,tipo,estado,circuito,municipio)
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


def eleccion_candidato(request):

    id_ele = request.GET['id']
    listar_elecciones = Eleccion.objects.filter(id=id_ele)
    listar = ExitPoll.objects.filter(eleccion_id=id_ele)
    candidatos = Candidatos.objects.all()
    listar_c = listar.values('candidatos_id')
    candi = Candidatos.objects.filter(pk__in=listar_c).values('id','nombre', 'apellido')
    return HttpResponse(json.dumps(list(candi)), content_type='application/json')

