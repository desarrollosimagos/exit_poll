#  encoding:utf-8
from django.views.generic import CreateView, ListView, UpdateView, View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import Encuesta
from apps.registro.preguntas.models import Preguntas
from apps.registro.respuestas.models import Respuestas
from .forms import EncuestaForm
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import base64
import json
from django.db import connection, transaction
import sys
from .formato_reportes import ver_encuesta


@login_required(login_url='/')
def RegistrarEncuesta(request):
    """ Vista basada en Metodos o funciones: (`Registrar`)"""
    #obj_reg_enc = Encuesta.objects.get(id=pk)
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT cod_encuesta FROM encuestas_encuesta ORDER BY cod_encuesta DESC LIMIT 1')
        c = cursor.fetchone()
        id_count = c[0] + 1

    except:
        id_count = 1

    if request.method == 'POST':
        formulario = EncuestaForm(request.POST, request.FILES)
        if formulario.is_valid():
            new_reg_encuesta = formulario.save(commit=False)
            new_reg_encuesta.save()
            pk = new_reg_encuesta.id
            return HttpResponseRedirect('/encuestas/editarencuesta/'+str(pk))
    else:
        formulario = EncuestaForm()
    ctx = {'formulario': formulario, 'cod_encuesta': id_count}
    return render_to_response('registro/encuesta/encuesta.html', ctx,  context_instance=RequestContext(request))


@login_required(login_url='/')
def EditarEncuesta(request, pk):
    """ Vista basada en Metodos o funciones: (`modificar`)"""
    obj_reg_enc = Encuesta.objects.get(id=pk)

    pregun = Preguntas.objects.all()
    preguntas = pregun.filter(cod_encuesta=pk).values('id','cod_pregunta', 'pregunta', 'tipo').order_by('cod_pregunta')

    if request.method == 'POST':
        obj_reg_edit_enc = EncuestaForm(request.POST, request.FILES, instance=obj_reg_enc)

        if obj_reg_edit_enc.is_valid():
            new_reg_enc = obj_reg_edit_enc.save(commit=False)
            new_reg_enc.user = request.user.username
            new_reg_enc.save()
            return HttpResponseRedirect('/encuestas/')
    else:
        obj_reg_edit_enc = EncuestaForm(instance=obj_reg_enc)
    ctx = {'obj_reg_edit_enc': obj_reg_edit_enc, 'obj_reg_enc': obj_reg_enc, 'obj_pre': preguntas}
    return render_to_response('registro/encuesta/modificar.html', ctx,
                              context_instance=RequestContext(request))


class ListarEncuesta(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    :param paginate_by: Genera la paginacion de los registros en base a la cantidad definida.
    """
    model = Encuesta
    template_name = 'registro/encuesta/listar.html'
    # context_object_name = "listar_encuestas"

    def get_context_data(self, **kwargs):
        context = {}
        usuario_id = self.request.user.id

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
            encuestas = Encuesta.objects.all()
        else:
            encuestas = Encuesta.objects.all()
            encuestas = encuestas.filter(user_create_id=usuario_id)
            encuestas = encuestas.order_by('id').reverse()

        context['listar_encuestas'] = encuestas
        return context


class BorrarEncuesta(CreateView):

    def post(self, request, *args, **kwargs):
        response_data = {}
        id_reg = self.request.POST.get('id')
        Encuesta.objects.filter(id=id_reg).delete()
        id_pre = Preguntas.objects.filter(cod_encuesta = id_reg).values('id')
        Respuestas.objects.filter(cod_pregunta__in = id_pre).delete()
        Preguntas.objects.filter(cod_encuesta = id_reg).delete()

        existe = Encuesta.objects.filter(id=id_reg).exists()
        if existe is False:
            response_data['delete'] = 'ok'
            data = HttpResponse(json.dumps(response_data),content_type='application/json')
            return data

    def get(self, request, *args, **kwargs):
        pk_enc = self.kwargs['pk']

        encuesta = Encuesta.objects.get(id=pk_enc)
        encuesta.delete()

        return HttpResponseRedirect('/encuestas')


class FinalizarEncuesta(UpdateView):

    def post(self, request, *args, **kwargs):
        response_data = {}
        id_reg = self.request.POST.get('id') #id de la encuesta
        Encuesta.objects.filter(id=id_reg).update()
        existe = Encuesta.objects.filter(id=id_reg).exists() #Existe esa encuesta
        existe_p = Preguntas.objects.filter(cod_encuesta=id_reg).exists() #Existe pregunta(s) a esa encuesta

        if existe_p is True:
            cursor = connection.cursor()
            sql_estatus = ('UPDATE encuestas_encuesta SET estatus=2 WHERE id=%s')
            cursor.execute(sql_estatus, [id_reg])
            # print('pass')
            response_data['update'] = 'ok'
            data = HttpResponse(json.dumps(response_data),content_type='application/json')
            return data
        else:
            response_data['update'] = 'negativo'
            data = HttpResponse(json.dumps(response_data),content_type='application/json')
            return data
        return HttpResponseRedirect('/encuestas')


class CerrarEncuesta(UpdateView):

    def post(self, request, *args, **kwargs):
        response_data = {}
        id_reg = self.request.POST.get('id')
        Encuesta.objects.filter(id=id_reg).update()
        existe = Encuesta.objects.filter(id=id_reg).exists()
        
        cursor = connection.cursor()
        sql_estatus = ('UPDATE encuestas_encuesta SET estatus=3 WHERE id=%s')
        cursor.execute(sql_estatus, [id_reg])
        
        if existe is True:

            response_data['update'] = 'ok'
            data = HttpResponse(json.dumps(response_data),content_type='application/json')
            return data
        
        return HttpResponseRedirect('/encuestas')

class VerEncuesta(View):
    model = Encuesta
    
    def get(self, request, *args, **kwargs):

        id_enc = kwargs.get('encuesta',None)

        cursor = connection.cursor()
        sql_det = "SELECT id, cod_encuesta, nombre, estatus "
        sql_det += " FROM encuestas_encuesta "
        sql_det += " WHERE id = %s "
        cursor.execute(sql_det, [id_enc])
        row = dictfetchall(cursor)

        nombre, archivo = ver_encuesta.ver_encuesta(id_enc)
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
