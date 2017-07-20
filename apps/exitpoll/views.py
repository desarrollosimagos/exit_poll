#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

from django.views.generic import CreateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from .models import ExitPoll
from apps.candidatos.models import Candidatos
from apps.elecciones.models import Eleccion
from apps.tipos.categoria_eleccion.models import Categoria
from apps.tipos.tipo_eleccion.models import Tipo_eleccion
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.circuitos.models import Circuito
from apps.topologia.sectores.models import Sector
# from apps.centro_votacion.models import Centros
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ExitPollForm
from django.views.generic.edit import FormView
from apps.tipos.tipo_eleccion.models import Tipo_eleccion
from apps.topologia.parroquias.models import Parroquia
from apps.topologia.poligonales.models import Poligonal
from django.db import connection
from apps.grupo_etareo.models import Grupo_Etareo
from apps.partidos.models import Partidos


class RegistrarExitPoll(CreateView):
    """ Vista basada en clase: (`Registrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminado el registro
        satisfactoriamente.
    :param fields:
    """
    template_name = 'exitpoll/exitpoll.html'
    model = ExitPoll
    success_url = reverse_lazy("listar_exitpoll")
    fields = ['candidatos', 'eleccion', 'user_create', 'estado', 'municipio', 'parroquia', 'circuito', 'sector', 'poligonal']

    def get_context_data(self, **kwargs):
        """ Vista basada en Clases con un metodo: (`Registrar`). """

        context = super(RegistrarExitPoll, self).get_context_data(**kwargs)
        listar_elecciones = Eleccion.objects.all()
        listar_elecciones = listar_elecciones.filter(ele_activa='TRUE')
        listar_candidato = Candidatos.objects.all()
        listar_estado = Estado.objects.all()
        #listar_sectores = Estado.objects.all()

        context['listar_candidato'] = listar_candidato
        context['listar_elecciones'] = listar_elecciones
        context['listar_estados'] = listar_estado
        #context['listar_estados'] = listar_estado

        return context

    def post(self, request, *args, **kwargs):

        bandera = request.POST.get('bandera')
        candidatos = request.POST.get('candidatos')
        eleccion = request.POST.get('eleccion')
        municipio = request.POST.get('municipio')
        parroquia = request.POST.get('parroquia')
        existe = ExitPoll.objects.filter(candidatos_id=candidatos, eleccion_id=eleccion).exists()
        if existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            #add = form.save(commit=False)
            #if municipio is None:
            #        add.municipio = 0
            #
            #if parroquia is None:
            #    add.parroquia = 0

            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/exitpoll/')


class aggregated_row(object):
    def __init__(self, id_exit):
        self.id_exit = id_exit


class ListarExitPoll(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = ExitPoll
    template_name = 'exitpoll/listar.html'

    def get_context_data(self, **kwargs):
        """ Vista basada en Clases con un metodo: (`Registrar`). """

        context = super(ListarExitPoll, self).get_context_data(**kwargs)

        cursor = connection.cursor()
        sql = "SELECT ex_e.id, e_e.nombre AS exitpoll, c_c.nombre || ' ' || c_c.apellido AS nombres, COALESCE(es_es.estado,'') AS estado, COALESCE(mun.municipio,'') AS municipio, COALESCE(par.parroquia, '') AS parroquia, COALESCE('Nro. ' || cir.n_circuito,'') AS circuito, COALESCE(sec.sector,'') AS sector, COALESCE(pol.poligonal,'') AS poligonal"
        sql += " FROM exitpoll_exitpoll AS ex_e"
        sql += " INNER JOIN elecciones_eleccion AS e_e ON ex_e.eleccion_id=e_e.id"
        sql += " INNER JOIN candidatos_candidatos AS c_c ON ex_e.candidatos_id=c_c.id"
        sql += " LEFT JOIN estados_estado AS es_es ON ex_e.estado_id=es_es.cod_estado"
        sql += " LEFT JOIN municipios_municipio AS mun ON ex_e.municipio=mun.cod_municipio"
        sql += " LEFT JOIN parroquias_parroquia AS par ON ex_e.parroquia=par.cod_parroquia"
        sql += " LEFT JOIN circuitos_circuito AS cir ON ex_e.circuito=cir.id"
        sql += " LEFT JOIN sectores_sector AS sec ON ex_e.sector=sec.cod_s"
        sql += " LEFT JOIN poligonales_poligonal AS pol ON ex_e.poligonal=pol.cod_pol::integer"

        cursor.execute(sql)

        rows = dictfetchall(cursor)

        context['listar_exitpoll'] = rows

        return context


class BorrarExitPoll(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
         satisfactoriamente.
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = ExitPoll
    template_name = 'exitpoll/borrar.html'
    context_object_name = "borrar_exitpoll"
    success_url = reverse_lazy("listar_exitpoll")


class ListarCandidatos(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param mlistar_votosodel: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = ExitPoll
    template_name = 'exitpoll/candidatos.html'
    context_object_name = "listar_exitpoll"

    def get_context_data(self, **kwargs):
        """ Vista basada en Clases con un metodo: (`Registrar`). """
        id_ele = self.kwargs['pk']
        id_grupo = self.kwargs['grupo']
        id_sexo = self.kwargs['sexo']
        id_estado = self.kwargs['estado']
        id_circuito = self.kwargs['circuito']
        id_municipio = self.kwargs['municipio']
        listar_elecciones = Eleccion.objects.get(id=id_ele)
        context = super(ListarCandidatos, self).get_context_data(**kwargs)
        # listar = ExitPoll.objects.filter(eleccion_id=id_ele)

        for x in id_ele:
            u = id_ele
            
            cursor = connection.cursor()
            sql_partido = " SELECT c.id, CONCAT(c.nombre,' ',c.apellido) nom_ape, c.foto, p.foto_partido"
            sql_partido += " FROM exitpoll_exitpoll AS ex "
            sql_partido += " INNER JOIN candidatos_candidatos c ON c.id = ex.candidatos_id "
            sql_partido += " INNER JOIN partidos_partidos p ON p.id = c.part_politico_id "
            sql_partido += " WHERE ex.eleccion_id=%s ORDER BY c.nombre "
            cursor.execute(sql_partido, [u])
            todo = dictfetchall(cursor)

        listar_can = ExitPoll.objects.filter(eleccion_id=id_ele, estado_id=id_estado)

        context['id_sexo'] = id_sexo
        context['id_grupo'] = id_grupo
        context['id_estado'] = id_estado
        context['id_circuito'] = id_circuito
        context['id_municipio'] = id_municipio
        # context['listar'] = listar
        context['listar_elecciones'] = listar_elecciones.nombre
        context['listar_id'] = listar_elecciones.id
        
        context['todo'] = todo
        return context


class MenuMovil(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    
    """
    model = ExitPoll
    template_name = 'exitpoll/menumovil.html'
    context_object_name = "listar_exitpoll"

    def get_context_data(self, **kwargs):
        """ Vista basada en Clases con un metodo: (`Registrar`). """

        context = super(MenuMovil, self).get_context_data(**kwargs)
        listar_elecciones = Eleccion.objects.all()
        list_estados = Estado.objects.all()
        listar = listar_elecciones.filter(ele_activa='TRUE')
        edad = []
        for i in range(18,101):
            # edad = i
            edad.append(i)
        context['edad'] = edad
        context['listar'] = listar
        context['list_estados'] = list_estados
        return context

import json


def exit_poll_ajax(respuestas):
        """ Metodo que en base a la eleccion seleccionado se filtran las categorias y el tipo de eleccion relacionados a el y los datos
        serializados son validados en el metodo ajax ubicado en /static/js/validaciones.js
        """
        response_data = {}
        id_est = respuestas.GET['id']
        queryset = Eleccion.objects.all()
        queryset = queryset.filter(id=id_est)
        id_tipo = queryset.values('tipo_eleccion')
        
        queryset = queryset.select_related('categoria_eleccion')

        categoria_id = queryset.values('categoria_eleccion_id')

        queryset_tipo = Tipo_eleccion.objects.all()
        tipo_ele = queryset_tipo.filter(id=id_tipo)

        for n in queryset:
            cate = n.categoria_eleccion
            id_cate = n.id

        for n in tipo_ele:
            tipo = n.tipo
            nivel_cat = n.niveles
            id_tipo = n.id

        response_data['categoria'] = str(cate)
        response_data['tipo'] = str(tipo)
        response_data['nivel'] = str(nivel_cat)
        response_data['id_cate'] = str(id_cate)
        response_data['id_tipo'] = str(id_tipo)

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def dictfetchall(cursor):
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
