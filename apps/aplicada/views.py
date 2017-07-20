#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from apps.registro.encuestas.models import Encuesta
from apps.registro.preguntas.models import Preguntas
from apps.registro.respuestas.models import Respuestas
from apps.aplicada.models import EncuestaResultado
from apps.topologia.estados.models import Estado
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from apps.registro.encuestas.serializers import EncuestaSerializer
from apps.registro.respuestas.serializers import RespuestasSerializer
# from apps.aplicada.serializers import RespuestasSerializer
from rest_framework import generics, status
import json
from django.db import connection
from apps.ip_equipo.models import IpEquipo


class EncuestaWeb(CreateView):

    model = Encuesta
    template_name = 'encuesta/encuesta_web.html'
    serializer_class = EncuestaSerializer

    def get_context_data(self,  **kwargs):
        """ Vista basada en Clases con un metodo: (`Registrar`). """
        context = super(EncuestaWeb, self).get_context_data(**kwargs)
        pk_res = self.kwargs['cod_pregunta']
        queryset = Encuesta.objects.all().filter(id=pk_res)
        queryset_e = queryset.values('estatus')[0]['estatus']
        queryset_t = queryset.values('tipo')[0]['tipo']
        ip = self.request.META['REMOTE_ADDR']

        cursor = connection.cursor()
        sql_tipo = " SELECT tipo_aplicacion FROM encuestas_encuesta "
        sql_tipo += " WHERE id= %s"
        cursor.execute(sql_tipo, [pk_res])
        row2 = dictfetchall(cursor)
        tipo = row2[0]['tipo_aplicacion']

        if tipo == 2:
            existe = IpEquipo.objects.filter(cod_encuesta=pk_res, ip_equipo=ip).exists()
        else:
            existe = False

        if existe == True:
            continua = '2' #No Carga
        else:
            continua = '1' #Si Carga

        sql_numero = " SELECT num_encuestado FROM aplicada_encuestaresultado WHERE cod_encuesta = %s ORDER BY num_encuestado DESC LIMIT 1"
        cursor.execute(sql_numero, [pk_res])
        row = dictfetchall(cursor)
        num = 0
        if row == []:
            num_encuesta = 1
        else:
            num = row[0]['num_encuestado']
            num_encuesta = num + 1

        list_estados = Estado.objects.all()
        context['list_estados'] = list_estados
        context['num_encuesta'] = num_encuesta
        context['encuesta'] = pk_res
        context['estatus'] = queryset_e
        context['tipo'] = queryset_t
        context['cookies_id'] = self.request.META['REMOTE_ADDR']
        context['continua'] = continua
        return context


class EncuestaWebView(generics.ListAPIView):

    model = Encuesta
    serializer_class = RespuestasSerializer
    lookup_field = 'pregunta'

    def get_queryset(self):

        id_enc = self.kwargs['cod_pregunta']
        if id_enc is not None:
            queryset = Encuesta.objects.all().filter(id=id_enc)
            queryset_pre = Preguntas.objects.all().filter(cod_encuesta=id_enc)
            queryset_res = Respuestas.objects.all().filter(cod_pregunta_id=queryset_pre).order_by('id')
            # queryset = queryset.filter(id=id_enc)
            if queryset_res.exists():
                return queryset_res
            else:
                raise NotFound()


class GuardarEncuestas(CreateView):

    template_name = 'encuesta/encuesta.html'
    model = EncuestaResultado

    def post(self, request, *args, **kwargs):
        response_data = {}

        id_res = self.request.POST.get('id')
        id_est = self.request.POST.get('estado')
        id_mun = self.request.POST.get('municipio')
        edad = self.request.POST.get('edad')
        sexo = self.request.POST.get('sexo')
        ip_equipo = self.request.POST.get('ip_equipo')

        ids = id_res.split(',')

        # Con el Id de las Respuestas, consulto el
        # Id de la Encuesta a travez de las Preguntas
        for h in ids:
            u = h.split('_')[0]
            cursor = connection.cursor()
            sql_cod = ' SELECT pp.cod_encuesta id_encuesta'
            sql_cod += ' FROM respuestas_respuestas AS rr '
            sql_cod += ' INNER JOIN preguntas_preguntas AS pp ON pp.id = rr.cod_pregunta_id'
            sql_cod += ' where rr.id = %s'
            cursor.execute(sql_cod, [u])
            row = dictfetchall(cursor)
            id_enc = row[0]['id_encuesta']

        # Consulto el tipo de aplicación de la encuesta
        cursor = connection.cursor()
        sql_tipo = " SELECT tipo_aplicacion FROM encuestas_encuesta "
        sql_tipo += " WHERE id= %s"
        cursor.execute(sql_tipo, [id_enc])
        row2 = dictfetchall(cursor)
        tipo = row2[0]['tipo_aplicacion']

        # Si es de Tipo 2 (No Continua)
        # Guardo la Ip del equipo y el Id de la encuesta
        if tipo == 2:
            sql_ip = "INSERT INTO ip_equipo_ipequipo (cod_encuesta, ip_equipo) "
            sql_ip += " VALUES ('"+str(id_enc)+"','"+str(ip_equipo)+"')"
            cursor.execute(sql_ip)

        # Consulto el ultimo número de encuestado
        # Si no hay es 1 sino le sumo +1 al ultimo
        sql_numero = " SELECT num_encuestado FROM aplicada_encuestaresultado WHERE cod_encuesta = %s ORDER BY num_encuestado DESC LIMIT 1"
        cursor.execute(sql_numero, [id_enc])
        row2 = dictfetchall(cursor)
        num = 0
        if row2 == []:
            can = 1
        else:
            num = row2[0]['num_encuestado']
            can = num + 1
        # Guardo cada una de las respuesta con los datos del encuestado
        for l in ids:
            m = l.split('_')[0]
            j = l.split('_')[1]

            cursor = connection.cursor()
            # Si la respuesta es cerrada
            if j == 'no':
                sql_guardar = "INSERT INTO aplicada_encuestaresultado (cod_respuesta, cod_encuesta, num_encuestado, grupo_etareo, sexo, estado, municipio) "
                sql_guardar += "VALUES ('"+str(m)+"','"+str(id_enc)+"','"+str(can)+"','"+str(edad)+"','"+str(sexo)+"','"+str(id_est)+"','"+str(id_mun)+"')"
            # Si la respuesta es abierta
            else:
                sql_guardar = "INSERT INTO aplicada_encuestaresultado (cod_respuesta, otras, cod_encuesta, num_encuestado, grupo_etareo, sexo, estado, municipio) "
                sql_guardar += "VALUES ('"+str(m)+"','"+str(j)+"','"+str(id_enc)+"','"+str(can)+"','"+str(edad)+"','"+str(sexo)+"','"+str(id_est)+"','"+str(id_mun)+"')"
            cursor.execute(sql_guardar)

        response_data['status'] = 'Guardado'

        return HttpResponse(json.dumps(response_data), content_type='application/json')


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
