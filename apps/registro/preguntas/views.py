from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import Preguntas
from .forms import PreguntasForm
from apps.registro.encuestas.models import Encuesta
from apps.registro.respuestas.models import Respuestas
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import base64
import json
from django.db import connection, transaction


class RegistrarPregunta(CreateView):

    template_name = 'registro/encuesta/modificar.html'
    model = Preguntas

    def post(self, request, *args, **kwargs):
        accion = self.request.POST.get('bandera')
        cod_encuesta = self.request.POST.get('cod')
        response_data = {}
        if accion == 'encuesta':
            cod_pregunta = 1
            queryset = Preguntas.objects.all()
            queryset = queryset.filter(cod_encuesta=cod_encuesta).order_by('-cod_pregunta')[:1]
            queryset = queryset.values('cod_pregunta')

            if queryset.exists():
                cod_pregunta = queryset[0]['cod_pregunta'] + 1
            response_data['cod_pregunta'] = cod_pregunta
        else:

            form_class = self.get_form_class()
            form = self.get_form(form_class)
            add = form.save(commit=False)
            if form.is_valid():
                add.save()
                ultimo = add.id
                response_data['status'] = 'Guardado'
                response_data['id'] = ultimo
                return HttpResponse(json.dumps(response_data), content_type='application/json')
            else:
                return HttpResponse('2')
        return HttpResponse(json.dumps(response_data), content_type='application/json')


class EditarPregunta(UpdateView):
    """ Vista basada en clase: (`Editar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminada la edicion del
        registro satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Preguntas
    template_name = 'registro/encuesta/modificar_pregunta.html'
    context_object_name = "editar_pregunta"
    success_url = reverse_lazy("listar_encuestas")

    def get_context_data(self, **kwargs):

        context = super(EditarPregunta, self).get_context_data(**kwargs)
        pk_pre = self.kwargs['pk']
        preguntas = Preguntas.objects.all()
        cod_enc = preguntas.filter(pk=pk_pre).values('cod_encuesta')
        encuesta = Encuesta.objects.all()
        nom_enc = encuesta.filter(pk=cod_enc)
        nombre = nom_enc[0]

        respuesta = Respuestas.objects.all()
        respuestas = respuesta.filter(cod_pregunta_id=pk_pre).values('id','cod_respuesta', 'respuesta', 'tipo')

        context['nombre_encuesta'] = nombre
        context['lista_respuestas'] = respuestas
        return context

class BorrarPreguntas(CreateView):

    def post(self, request, *args, **kwargs):
        response_data = {}
        id_reg = self.request.POST.get('id')
        Preguntas.objects.filter(id=id_reg).delete()
        existe = Preguntas.objects.filter(id=id_reg).exists()
        if existe is False:
            response_data['delete'] = 'ok'
            data = HttpResponse(json.dumps(response_data),content_type='application/json')
            return data

    def get(self, request, *args, **kwargs):
        pk_pregunta = self.kwargs['pk']

        pregunta = Preguntas.objects.get(id=pk_pregunta)
        pregunta.delete()
        return HttpResponseRedirect('/encuestas')
    


