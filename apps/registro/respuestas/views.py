from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from apps.registro.encuestas.models import Encuesta
from apps.registro.preguntas.models import Preguntas
from .models import Respuestas
from .forms import RespuestasForm
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import base64
import json
from django.db import connection, transaction


class RegistrarRespuestas(CreateView):

    template_name = 'registro/encuesta/modificar.html'
    model = Respuestas

    def post(self, request, *args, **kwargs):
        accion = self.request.POST.get('bandera')
        cod_pregunta = self.request.POST.get('cod')
        response_data = {}
        if accion == 'pregunta':
            cod_respuesta = 1
            queryset = Respuestas.objects.all()
            queryset = queryset.filter(cod_pregunta_id=cod_pregunta).order_by('-cod_respuesta')[:1]
            queryset = queryset.values('cod_respuesta')
            
            if queryset.exists():
                cod_respuesta = queryset[0]['cod_respuesta'] + 1        
            response_data['cod_respuesta'] = cod_respuesta
        else:

            form_class = self.get_form_class()
            form = self.get_form(form_class)
            add = form.save(commit=False)
            if form.is_valid():
                add.save()

                response_data['status'] = 'Guardado'

                return HttpResponse(json.dumps(response_data), content_type='application/json')
            else:
                return HttpResponse('2')

        return HttpResponse(json.dumps(response_data), content_type='application/json')


class EditarRespuestas(UpdateView):
    """ Vista basada en clase: (`Editar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminada la edicion del
        registro satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Respuestas
    template_name = 'registro/encuesta/modificar_respuesta.html'
    context_object_name = "editar_respuestas"
    success_url = reverse_lazy("listar_encuestas")

    def get_context_data(self, **kwargs):

        context = super(EditarRespuestas, self).get_context_data(**kwargs)
        pk_res = self.kwargs['pk']
        respuesta = Respuestas.objects.all()
        cod_enc = respuesta.filter(pk=pk_res).values('cod_pregunta')

        pregunta = Preguntas.objects.all()
        cod_encuesta = pregunta.filter(pk=cod_enc).values('cod_encuesta')

        encuesta = Encuesta.objects.all()
        nom_enc = encuesta.filter(pk=cod_encuesta)
        nombre = nom_enc[0]

        context['nombre'] = nombre
        #context['editar_respuestas'] = editar_respuestas

        return context


class BorrarRespuestas(CreateView):

    def post(self, request, *args, **kwargs):
        response_data = {}
        id_reg = self.request.POST.get('id')
        Respuestas.objects.filter(id=id_reg).delete()
        existe = Respuestas.objects.filter(id=id_reg).exists()
        if existe is False:
            response_data['delete'] = 'ok'
            data = HttpResponse(json.dumps(response_data),content_type='application/json')
            return data

    def get(self, request, *args, **kwargs):
        pk_respuesta = self.kwargs['pk']

        respuesta = Respuestas.objects.get(id=pk_respuesta)
        respuesta.delete()
        return HttpResponseRedirect('/encuestas')
