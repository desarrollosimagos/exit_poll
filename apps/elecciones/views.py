# -*- encoding: utf-8 -*-# -*- encoding: utf-8 *

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Eleccion
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .forms import EleccionForm
from apps.tipos.categoria_eleccion.models import Categoria
from apps.tipos.tipo_eleccion.models import Tipo_eleccion
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.exitpoll.models import ExitPoll


@login_required(login_url='/')
def RegistrarEleccion(request):
    """ Vista basada en Metodos o funciones: (`Registrar`). """
    list_categoria = Categoria.objects.all()  # Modelo de consulta a Categoria
    list_tipo = Tipo_eleccion.objects.all()  # Modelo de consulta a Tipo_eleccion
    if request.method == 'POST':
        bandera = request.POST.get('bandera')
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria_eleccion')
        tipo_eleccion = request.POST.get('tipo_eleccion')
        existe = Eleccion.objects.filter(nombre=nombre).exists()
        if existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_reg_eleccion = EleccionForm(request.POST, request.FILES)
            if form_reg_eleccion.is_valid():
                new_reg_eleccion = form_reg_eleccion.save(commit=False)
                new_reg_eleccion.save()
            return HttpResponseRedirect('/elecciones/')
    else:
        form_reg_eleccion = EleccionForm()
    ctx = {'form_reg_eleccion': form_reg_eleccion, 'list_categoria': list_categoria,
           'list_tipo': list_tipo}  # ctx = Contexto
    return render_to_response('elecciones/eleccion.html',
                              ctx, context_instance=RequestContext(request))


@login_required(login_url='/')
def EditarEleccion(request, pk):
    """ Vista basada en Metodos o funciones: (`Modificar`)."""
    list_categoria = Categoria.objects.all()  # Modelo de consulta a Categoria
    list_tipo = Tipo_eleccion.objects.all()  # Modelo de consulta a Tipo_eleccion
    obj_eleccion = Eleccion.objects.get(id=pk)
    if request.method == 'POST':
        form_eleccion = EleccionForm(request.POST, request.FILES, instance=obj_eleccion)
        if form_eleccion.is_valid():
            edit_regelector = form_eleccion.save(commit=False)
            edit_regelector.save()
            return HttpResponseRedirect('/elecciones/')
    else:
        form_eleccion = EleccionForm(instance=obj_eleccion)
    ctx = {'form_eleccion': form_eleccion, 'obj_eleccion': obj_eleccion, 'list_categoria': list_categoria,
           'list_tipo': list_tipo, }
    return render_to_response('elecciones/modificar.html',
                              ctx, context_instance=RequestContext(request))


def tipo_ajax(request):
    id_cat = request.GET['id']
    tipo = Tipo_eleccion.objects.filter(categoria_id=id_cat)
    data = serializers.serialize('json', tipo, fields=('id', 'tipo'))

    return HttpResponse(data, content_type='application/json')


class ListarEleccion(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista

    """
    model = Eleccion
    template_name = 'elecciones/listar.html'
    context_object_name = "listar_eleccion"
    form_class = EleccionForm

    def post(self, request, *args, **kwargs):

        pk_usuario = self.request.POST.get('pk')
        status = self.request.POST.get('status')

        #Validamos el status
        if status == 'false':
            status = False
        else:
            status = True

        #Buscamos el id(pk) del usuario en el modelo de Usuario
        eleccion = Eleccion.objects.filter(id=pk_usuario)
        eleccion.update(
            ele_activa=status
        )
        return HttpResponse('exito')

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ListarEleccion, self).get_context_data(**kwargs)
        # Agregamos un QuerySet
        context['list_t'] = Tipo_eleccion.objects.all()
        return context


class BorrarEleccion(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
         satisfactoriamente.
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Eleccion
    template_name = 'elecciones/borrar.html'
    context_object_name = "borrar_eleccion"
    success_url = reverse_lazy("listar_eleccion")

    def get_context_data(self, **kwargs):
        context = super(BorrarEleccion, self).get_context_data(**kwargs)
        id_ele = self.kwargs['pk']
        ele = ExitPoll.objects.all()
        existe = ele.filter(eleccion_id=id_ele)
        cantidad = len(existe)
        
        context['cantidad'] = cantidad
        return context
