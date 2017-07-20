#encoding:utf-8
from django.views.generic import CreateView, TemplateView, DetailView, ListView, View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from apps.votacion.models import Votacion
from apps.candidatos.models import Candidatos
from apps.exitpoll.models import ExitPoll
from apps.elecciones.models import Eleccion
from apps.grupo_etareo.models import Grupo_Etareo
from django.core import serializers
from django.db.models import Count
import json
import sys
from django.http import HttpResponse
from django.template import RequestContext
#import class_pdf
from django.db import connection, transaction
import time
from apps.reportes.reportes_detallados.formato_reportes import reporte_candidato_detallado
from apps.reportes.reportes_detallados.formato_reportes import reporte_candidato_sencillo
from apps.reportes.reportes_detallados.formato_reportes import reporte_listado_exit_datallado
from apps.reportes.reportes_detallados.formato_reportes import reporte_listado_exit_sencillo
from django.conf import settings


class ListarFiltros(TemplateView):

    #model = Votacion
    template_name = 'reportes/detallados.html'

    def get_context_data(self, **kwargs):
        context = super(ListarFiltros, self).get_context_data(**kwargs)
        eleccion = Eleccion.objects.all()
        candidatos = Candidatos.objects.all()
        context['eleccion'] = eleccion
        context['candidatos'] = candidatos

        return context


class ReporteExitPollsCandidatos(View):

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        fecha_hora = time.strftime("%d/%m/%Y")
        fecha = time.strftime("%d-%m-%Y")
        sys.setdefaultencoding("utf-8")
        desde = kwargs.get('from_date', None)
        hasta = kwargs.get('to_date', None)
        cursor = connection.cursor()
        sql_ele = "SELECT v.eleccion_id, e.nombre, COUNT(v.id) total FROM votacion_votacion v"
        sql_ele += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
        sql_ele += " WHERE e.fecha_create between %s and %s"
        sql_ele += " GROUP BY e.nombre, v.eleccion_id "
        cursor.execute(sql_ele,[desde,hasta])
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
            nombre, archivo = reporte_listado_exit_sencillo.reporte_listado_exit_sencillo(desde,hasta)
            response = HttpResponse(archivo.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="'+str(nombre)
    
            return response


class ReporteDetallado(View):

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        fecha_hora = time.strftime("%d/%m/%Y")
        fecha = time.strftime("%d-%m-%Y")
        sys.setdefaultencoding("utf-8")
        desde = kwargs.get('from_date', None)
        hasta = kwargs.get('to_date', None)

        cursor = connection.cursor()
        sql_ele = "SELECT v.eleccion_id, e.nombre, COUNT(v.id) total FROM votacion_votacion v"
        sql_ele += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
        sql_ele += " WHERE e.fecha_create  between %s and %s"
        sql_ele += " GROUP BY e.nombre, v.eleccion_id "
        cursor.execute(sql_ele,[desde,hasta])
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
            nombre, archivo = reporte_listado_exit_datallado.reporte_listado_exit_datallado(desde,hasta)
            response = HttpResponse(archivo.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="'+str(nombre)
            return response


class ReporteCandidatoBasico(View):

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        fecha_hora = time.strftime("%d/%m/%Y")
        fecha = time.strftime("%d-%m-%Y")
        sys.setdefaultencoding("utf-8")
        candidato = kwargs.get('candidato', None)

        cursor = connection.cursor()
        sql_id = "SELECT CONCAT(c.nombre,' ',c.apellido) nom_ape, v.eleccion_id id_e"
        sql_id += " FROM candidatos_candidatos c"
        sql_id += " INNER JOIN votacion_votacion v ON v.candidatos_id = c.id "
        sql_id += " WHERE c.id=%s GROUP BY c.nombre, c.apellido, v.eleccion_id "
        cursor.execute(sql_id, [candidato])
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
            nombre, archivo = reporte_candidato_sencillo.detallado_candidato_sencillo(candidato)
            response = HttpResponse(archivo.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="'+str(nombre)
            return response


class ReporteCandidatoDetallado(View):

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        fecha_hora = time.strftime("%d/%m/%Y")
        fecha = time.strftime("%d-%m-%Y")
        sys.setdefaultencoding("utf-8")
        candidato = kwargs.get('candidato', None)

        cursor = connection.cursor()
        sql_id = "SELECT CONCAT(c.nombre,' ',c.apellido) nom_ape, v.eleccion_id id_e"
        sql_id += " FROM candidatos_candidatos c"
        sql_id += " INNER JOIN votacion_votacion v ON v.candidatos_id = c.id "
        sql_id += " WHERE c.id=%s GROUP BY c.nombre, c.apellido, v.eleccion_id "
        cursor.execute(sql_id, [candidato])
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
            nombre, archivo = reporte_candidato_detallado.detallado_candidato_completo(candidato)
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
