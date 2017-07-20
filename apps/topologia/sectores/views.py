from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from apps.topologia.sectores.models import Sector
from django.views.generic.edit import FormView
from apps.topologia.sectores.forms import SectorForm
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.topologia.poligonales.models import Poligonal
from django.contrib.auth.decorators import login_required
from django.core import serializers


@login_required(login_url='/')
def RegistrarSector(request):
    """ Vista basada en Metodos o funciones: (`Registrar`) """
    list_estado = Estado.objects.all()
    if request.method == 'POST':
        bandera = request.POST.get('bandera')
        estado = request.POST.get('estado')
        cod_s = request.POST.get('cod_s')
        sector = request.POST.get('sector')
        existe = Sector.objects.filter(estado=estado, cod_s=cod_s).exists()
        existe_t = Sector.objects.filter(estado=estado, cod_s=cod_s, sector=sector).exists()
        if existe_t and bandera == 'true':
            return HttpResponse('existe_t')
        elif existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_reg_sector = SectorForm(request.POST, request.FILES)
            if form_reg_sector.is_valid():
                new_reg_sector = form_reg_sector.save(commit=False)
                new_reg_sector.save()
            return HttpResponseRedirect('/configuraciones/topologia/sectores/')
    else:
        form_reg_sector = SectorForm()
    ctx = {'form_reg_sector': form_reg_sector, 'list_estado': list_estado}
    return render_to_response('topologia/sectores/sectores.html',
                              ctx, context_instance=RequestContext(request))


@login_required(login_url='/')
def ActualizarSector(request, pk):
    """ Vista basada en Metodos o funciones: (`modificar`) """
    obj_reg_sec = Sector.objects.get(id=pk)
    list_estado = Estado.objects.all()
    list_mun = Municipio.objects.filter(estado_id=obj_reg_sec.estado_id)
    list_par = Parroquia.objects.filter(estado_id=obj_reg_sec.estado_id, municipio=obj_reg_sec.municipio)

    if request.method == 'POST':
        obj_reg_edit_sec = SectorForm(request.POST, request.FILES, instance=obj_reg_sec)
        if obj_reg_edit_sec.is_valid():
            new_reg_sector = obj_reg_edit_sec.save(commit=False)
            new_reg_sector.user = request.user.username
            new_reg_sector.save()
            return HttpResponseRedirect('/configuraciones/topologia/sectores/')
    else:
        obj_reg_edit_sec = SectorForm(instance=obj_reg_sec)
    ctx = {'obj_reg_edit_sec': obj_reg_edit_sec, 'obj_reg_sec': obj_reg_sec,
           'list_estado': list_estado, 'list_mun': list_mun, 'list_par': list_par}  # ctx = Contexto
    return render_to_response('topologia/sectores/modificar.html', ctx,
                              context_instance=RequestContext(request))


class ListarSector(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Sector
    template_name = 'topologia/sectores/listar.html'
    context_object_name = "listar_sectores"


    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ListarSector, self).get_context_data(**kwargs)
        # Agregamos un QuerySet
        context['list_m'] = Municipio.objects.all()
        context['list_p'] = Parroquia.objects.all()
        return context


class BorrarSector(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
        satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Sector
    template_name = 'topologia/sectores/borrar.html'
    context_object_name = "borrar_sector"
    success_url = reverse_lazy("listar_sectores")

    def get_context_data(self, **kwargs):
        context = super(BorrarSector, self).get_context_data(**kwargs)
        pk_sec = self.kwargs['pk']
        sector = Sector.objects.all()
        id_sec = sector.filter(pk=pk_sec).values('cod_s')
        id_par = sector.filter(pk=pk_sec).values('parroquia')
        id_mun = sector.filter(pk=pk_sec).values('municipio')
        id_est = sector.filter(pk=pk_sec).values('estado_id')

        pol = Poligonal.objects.all()
        existe = pol.filter(sector =id_sec ,parroquia=id_par, municipio=id_mun, estado_id=id_est)
        cantidad = len(existe)

        context['cantidad'] = cantidad

        return context
