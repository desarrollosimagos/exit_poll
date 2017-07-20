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
from apps.topologia.estados.models import Estado
from django.db.models import Count
import json
import sys
from django.http import HttpResponse
from django.template import RequestContext
import class_pdf
from django.db import connection, transaction
import time
from apps.reportes.reportes.formato_reportes import reporte_eleccion_grupo
from apps.reportes.reportes.formato_reportes import reporte_eleccion_candidatos
from apps.reportes.reportes.formato_reportes import reporte_eleccion_detallado
from apps.reportes.reportes.formato_reportes import reporte_eleccion_sexo


class ListarGrafica(TemplateView):

    #model = Votacion
    template_name = 'reportes/grafica.html'

    def get_context_data(self, **kwargs):
        context = super(ListarGrafica, self).get_context_data(**kwargs)
        listar = Eleccion.objects.all()
        list_estados = Estado.objects.all()
        
        context['list_estados'] = list_estados
        context['listar'] = listar
        return context

    def post(self, request, *args, **kwargs):
        id_ele = self.request.POST.get('id_eleccion')
        response_data = []
        context = super(ListarGrafica, self).get_context_data(**kwargs)
        bandera = request.POST.get('bandera')
        tipo = request.POST.get('tipo')
        estado = request.POST.get('estado')
        municipio = request.POST.get('municipio')
        circuito = request.POST.get('circuito')

        listar_elecciones = Eleccion.objects.filter(id=id_ele)
        listar = ExitPoll.objects.filter(eleccion_id=id_ele)
        if bandera == 'candidato':
            if tipo == '1':
                cand_id = listar.values('candidatos_id')
                queryset = Votacion.objects.filter(candidatos_id=cand_id, eleccion_id=id_ele).values('candidatos__nombre', 'candidatos__apellido').annotate(total=Count('candidatos_id'))
            elif tipo == '2':
                cand_id = listar.values('candidatos_id')
                queryset = Votacion.objects.filter(candidatos_id=cand_id, eleccion_id=id_ele, estado=estado).values('candidatos__nombre', 'candidatos__apellido').annotate(total=Count('candidatos_id'))
            elif tipo == '3':
                cand_id = listar.values('candidatos_id')
                queryset = Votacion.objects.filter(candidatos_id=cand_id, eleccion_id=id_ele, circuito=circuito).values('candidatos__nombre', 'candidatos__apellido').annotate(total=Count('candidatos_id'))
            else:
                cand_id = listar.values('candidatos_id')
                queryset = Votacion.objects.filter(candidatos_id=cand_id, eleccion_id=id_ele, municipio=municipio).values('candidatos__nombre', 'candidatos__apellido').annotate(total=Count('candidatos_id'))
                
        elif bandera == 'grupo':
            cursor = connection.cursor()
            sql_ele = " SELECT CONCAT (g.descripcion,' (',g.desde,'-',g.hasta,' Años)') descripcion, "
            if tipo == '1':
                sql_ele += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total "
            elif tipo == '2':
                sql_ele += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s AND estado="+str(estado)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total "
            elif tipo == '3':
                sql_ele += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s AND circuito="+str(circuito)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total "
            else:
                sql_ele += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s AND municipio="+str(municipio)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total "
            
            sql_ele += " FROM grupo_etareo_grupo_etareo AS g ORDER BY total DESC"

            cursor.execute(sql_ele, [id_ele])
            queryset = dictfetchall(cursor)

        elif bandera == 'sexo':
            cursor = connection.cursor()
            if tipo == '1':
                sql_sexo = "SELECT sexo, COUNT(sexo) total FROM votacion_votacion WHERE eleccion_id=%s GROUP BY sexo "
            elif tipo == '2':
                sql_sexo = "SELECT sexo, COUNT(sexo) total FROM votacion_votacion WHERE eleccion_id=%s AND estado="+str(estado)+" GROUP BY sexo "
            elif tipo == '3':
                sql_sexo = "SELECT sexo, COUNT(sexo) total FROM votacion_votacion WHERE eleccion_id=%s AND circuito="+str(circuito)+" GROUP BY sexo "
            else:
                sql_sexo = "SELECT sexo, COUNT(sexo) total FROM votacion_votacion WHERE eleccion_id=%s AND municipio="+str(municipio)+" GROUP BY sexo "
            cursor.execute(sql_sexo, [id_ele])
            queryset = dictfetchall(cursor)

        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1

        data = json.dumps(response_data)

        return HttpResponse(data, content_type='application/json')


class ReporteCandidato(View):

    template_name = 'reportes/grafica.html'
    model = Votacion

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):
        exitpoll = self.request.GET.get('exitpoll')
        tipo = self.request.GET.get('tipo')
        estado = self.request.GET.get('estado')
        circuito = self.request.GET.get('circuito')
        municipio = self.request.GET.get('municipio')
        reload(sys)
        sys.setdefaultencoding("utf-8")

        cursor = connection.cursor()
        sql_res = "SELECT CONCAT(c.nombre,' ',c.apellido) nom_ape, COUNT(v.candidatos_id) can_v, "
        if tipo == '1':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s), 2) porcentaje"
        elif tipo == '2':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.estado="+str(estado)+"), 2) porcentaje"
        elif tipo == '3':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.circuito="+str(circuito)+"), 2) porcentaje"
        else:
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.municipio="+str(municipio)+"), 2) porcentaje"
        sql_res += " FROM votacion_votacion v "
        sql_res += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
        sql_res += " INNER JOIN candidatos_candidatos c ON v.candidatos_id = c.id"
        if tipo == '1':
            sql_res += " WHERE v.eleccion_id=%s "
        elif tipo == '2':
            sql_res += " WHERE v.eleccion_id=%s AND v.estado="+str(estado)+""
        elif tipo == '3':
            sql_res += " WHERE v.eleccion_id=%s AND v.circuito="+str(circuito)+""
        else:
            sql_res += " WHERE v.eleccion_id=%s AND v.municipio="+str(municipio)+""
        sql_res += " GROUP BY v.candidatos_id, c.nombre, c.apellido ORDER BY porcentaje DESC"
        
        cursor.execute(sql_res, [exitpoll,exitpoll])
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
            nombre, archivo = reporte_eleccion_candidatos.detallado_eleccion_candidatos(exitpoll,tipo,estado,circuito,municipio)
            response = HttpResponse(archivo.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="'+str(nombre)

            return response


class ReporteGrupo(View):

    template_name = 'reportes/grafica.html'
    model = Votacion

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        sys.setdefaultencoding("utf-8")
        grupo = self.request.GET.get('grupo')
        tipo = self.request.GET.get('tipo')
        estado = self.request.GET.get('estado')
        circuito = self.request.GET.get('circuito')
        municipio = self.request.GET.get('municipio')

        cursor = connection.cursor()

        if tipo == '1':
            cursor.execute("SELECT v.grupo_etareo FROM votacion_votacion v WHERE v.eleccion_id="+str(grupo)+"")
        elif tipo == '2':
            cursor.execute("SELECT id from votacion_votacion WHERE eleccion_id="+str(grupo)+"AND estado="+str(estado)+" ")
        elif tipo == '3':
            cursor.execute("SELECT id from votacion_votacion WHERE eleccion_id="+str(grupo)+"AND circuito="+str(circuito)+" ")
        else:
            cursor.execute("SELECT id from votacion_votacion WHERE eleccion_id="+str(grupo)+"AND municipio="+str(municipio)+" ")
        row = dictfetchall(cursor)
        print row
        if len(row) == 0:
            response = "<body>"
            response += "<link rel='stylesheet' type='text/css' href='/static/css/bootstrap.css'>"
            response += "<script src='/static/js/bootstrap.min.js'></script>"
            response += "<img src='/static/img/disculpe.jpg' style='width:80%;margin-left:10%'/>"
            response += "<button title='Cerrar ventana' class='btn btn-danger' style='font-size:24px; width:20%; height: 10%; font-weight: bold; text-align: center;margin-left:40%' onclick=window.close()>Cerrar</button>"
            response += "<body>"
            return HttpResponse(response)
        else:
            nombre, archivo = reporte_eleccion_grupo.detallado_eleccion_grupo(grupo,tipo,estado,circuito,municipio)
            response = HttpResponse(archivo.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="'+str(nombre)

            return response


class ReporteSexo(View):

    template_name = 'reportes/grafica.html'
    model = Votacion

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        sys.setdefaultencoding("utf-8")
        sexo = self.request.GET.get('sexo')
        tipo = self.request.GET.get('tipo')
        estado = self.request.GET.get('estado')
        circuito = self.request.GET.get('circuito')
        municipio = self.request.GET.get('municipio')

        cursor = connection.cursor()
        sql_sexo = "SELECT COUNT(v.sexo) total, v.sexo sexo, "
        if tipo == '1':
            sql_sexo += " ROUND (COUNT (v.sexo) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s), 2) porcentaje"
        elif tipo == '2':
            sql_sexo += " ROUND (COUNT (v.sexo) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.estado="+str(estado)+"), 2) porcentaje"
        elif tipo == '3':
            sql_sexo += " ROUND (COUNT (v.sexo) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.circuito="+str(circuito)+"), 2) porcentaje"
        else:
            sql_sexo += " ROUND (COUNT (v.sexo) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.municipio="+str(municipio)+"), 2) porcentaje"
        sql_sexo += " FROM votacion_votacion v"
        sql_sexo += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
        sql_sexo += " INNER JOIN candidatos_candidatos c ON v.candidatos_id = c.id"
        if tipo == '1':
            sql_sexo += " WHERE v.eleccion_id=%s "
        elif tipo == '2':
            sql_sexo += " WHERE v.eleccion_id=%s AND v.estado="+str(estado)+""
        elif tipo == '3':
            sql_sexo += " WHERE v.eleccion_id=%s AND v.circuito="+str(circuito)+""
        else:
            sql_sexo += " WHERE v.eleccion_id=%s AND v.municipio="+str(municipio)+""
        sql_sexo += " GROUP BY v.sexo ORDER BY total DESC "
        cursor.execute(sql_sexo, [sexo,sexo])
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
            nombre, archivo = reporte_eleccion_sexo.reporte_eleccion_sexo(sexo,tipo,estado,circuito,municipio)
            response = HttpResponse(archivo.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="'+str(nombre)

            return response


class ReporteDetallado(View):

    template_name = 'reportes/grafica.html'
    model = Votacion

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        reload(sys)
        sys.setdefaultencoding("utf-8")
        detallado = self.request.GET.get('detallado')
        tipo = self.request.GET.get('tipo')
        estado = self.request.GET.get('estado')
        circuito = self.request.GET.get('circuito')
        municipio = self.request.GET.get('municipio')

        cursor = connection.cursor()
        sql_res = "SELECT CONCAT(c.nombre,' ',c.apellido) nom_ape, COUNT(v.candidatos_id) can_v, v.candidatos_id id_c, "
        if tipo == '1':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s), 2) porcentaje"
        elif tipo == '2':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s AND v.estado="+str(estado)+"), 2) porcentaje"
        elif tipo == '3':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s AND v.circuito="+str(circuito)+"), 2) porcentaje"
        else:
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s AND v.municipio="+str(municipio)+"), 2) porcentaje"
        sql_res += " FROM votacion_votacion v "
        sql_res += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
        sql_res += " INNER JOIN candidatos_candidatos c ON v.candidatos_id = c.id"
        if tipo == '1':
            sql_res += " WHERE v.eleccion_id=%s "
        elif tipo == '2':
            sql_res += " WHERE v.eleccion_id=%s AND v.estado="+str(estado)+" "
        elif tipo == '3':
            sql_res += " WHERE v.eleccion_id=%s AND v.circuito="+str(circuito)+" "
        else:
            sql_res += " WHERE v.eleccion_id=%s AND v.municipio="+str(municipio)+" "
        sql_res += " GROUP BY v.candidatos_id, c.nombre, c.apellido ORDER BY can_v DESC"
        
        cursor.execute(sql_res, [detallado,detallado])
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
            nombre, archivo = reporte_eleccion_detallado.detallado_eleccion_detallado(detallado,tipo,estado,circuito,municipio)
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


