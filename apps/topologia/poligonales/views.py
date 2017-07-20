from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from apps.topologia.sectores.models import Sector
from django.views.generic.edit import FormView
from apps.topologia.poligonales.forms import PoligonalForm
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.topologia.poligonales.models import Poligonal
from apps.exitpoll.models import ExitPoll
from django.contrib.auth.decorators import login_required
from django.core import serializers


@login_required(login_url='/login/')
def RegistrarPoligonal(request):
    """ Vista basada en Metodos o funciones: (`Registrar`) """
    list_estado = Estado.objects.all()

    if request.method == 'POST':
        bandera = request.POST.get('bandera')
        cod_pol = request.POST.get('cod_pol')
        #print cod_pol
        estado = request.POST.get('estado')
        existe = Poligonal.objects.filter(estado_id=estado, cod_pol=cod_pol).exists()
        print existe
        if existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_reg_poligonal = PoligonalForm(request.POST, request.FILES)
            if form_reg_poligonal.is_valid():
                new_reg_poligonal = form_reg_poligonal.save(commit=False)
                new_reg_poligonal.save()
            return HttpResponseRedirect('/configuraciones/topologia/poligonales/')
    else:
        form_reg_poligonal = PoligonalForm()
    ctx = {'form_reg_poligonal': form_reg_poligonal, 'list_estado': list_estado}
    return render_to_response('topologia/poligonales/poligonales.html',
                              ctx, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def ActualizarPoligonal(request, pk):
    """ Vista basada en Metodos o funciones: (`modificar`) """
    obj_reg_pol = Poligonal.objects.get(id=pk)
    list_estado = Estado.objects.all()
    list_mun = Municipio.objects.filter(estado_id=obj_reg_pol.estado_id)
    list_par = Parroquia.objects.filter(estado_id=obj_reg_pol.estado_id, municipio=obj_reg_pol.municipio)
    list_sec = Sector.objects.filter(estado_id=obj_reg_pol.estado_id, municipio=obj_reg_pol.municipio, parroquia=obj_reg_pol.parroquia)

    if request.method == 'POST':
        obj_reg_edit_pol = PoligonalForm(request.POST, request.FILES, instance=obj_reg_pol)
        if obj_reg_edit_pol.is_valid():
            new_reg_poligonal = obj_reg_edit_pol.save(commit=False)
            new_reg_poligonal.user = request.user.username
            new_reg_poligonal.save()
            return HttpResponseRedirect('/configuraciones/topologia/poligonales/')
    else:
        obj_reg_edit_pol = PoligonalForm(instance=obj_reg_pol)
    ctx = {'obj_reg_edit_pol': obj_reg_edit_pol, 'obj_reg_pol': obj_reg_pol,
           'list_estado': list_estado, 'list_mun': list_mun, 'list_par': list_par,
           'list_sec': list_sec}  # ctx = Contexto
    return render_to_response('topologia/poligonales/modificar.html', ctx,
                              context_instance=RequestContext(request))


class ListarPoligonal(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Poligonal
    template_name = 'topologia/poligonales/listar.html'
    context_object_name = "listar_poligonales"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ListarPoligonal, self).get_context_data(**kwargs)
        # Agregamos un QuerySet
        context['list_m'] = Municipio.objects.all()
        context['list_p'] = Parroquia.objects.all()
        context['list_s'] = Sector.objects.all()
        return context


class BorrarPoligonal(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
        satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Poligonal
    template_name = 'topologia/poligonales/borrar.html'
    context_object_name = "borrar_poligonal"
    success_url = reverse_lazy("listar_poligonales")

    def get_context_data(self, **kwargs):
        context = super(BorrarPoligonal, self).get_context_data(**kwargs)
        pk_sec = self.kwargs['pk']
        poligonal = Poligonal.objects.all()
        id_pol = poligonal.filter(pk=pk_sec).values('cod_pol')
        id_sec = poligonal.filter(pk=pk_sec).values('sector')
        id_par = poligonal.filter(pk=pk_sec).values('parroquia')
        id_mun = poligonal.filter(pk=pk_sec).values('municipio')
        id_est = poligonal.filter(pk=pk_sec).values('estado_id')

        ext = ExitPoll.objects.all()
        existe = ext.filter(poligonal=id_pol, sector=id_sec, parroquia=id_par, municipio=id_mun, estado_id=id_est)
        cantidad = len(existe)

        context['cantidad'] = cantidad

        return context


def BuscarAjaxSector(request):
    """ Metodo que en base al estado seleccionado y a su correspondiente municipio filtra las parroquias y sectores asociados, los datos son
    serializados y validados en el metodo ajax para el ubicado en /static/js/validaciones.js
    """
    id_est = request.GET['id_est']
    id_mun = request.GET['id_mun']
    id_parr = request.GET['id_parr']

    sectores = Sector.objects.filter(estado_id=id_est, municipio=id_mun, parroquia=id_parr)
    
    data = serializers.serialize('json', sectores, fields=('pk', 'sector'))

    return HttpResponse(data, content_type='application/json')
