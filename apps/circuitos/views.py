from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from .models import Circuito
from .forms import CircuitoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


@login_required(login_url='/')
def RegistrarCircuito(request):
    """ Vista basada en Metodos o funciones: (`Registrar`) """
    list_e = Estado.objects.all()
    list_m = Municipio.objects.all()
    if request.method == 'POST':
        bandera = request.POST.get('bandera')
        n_circuito = request.POST.get('n_circuito')
        estado = request.POST.get('estado')
        existe = Circuito.objects.filter(n_circuito=n_circuito, estado=estado).exists()
        if existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_reg_cir = CircuitoForm(request.POST, request.FILES)
            if form_reg_cir.is_valid():
                new_reg_cir = form_reg_cir.save(commit=False)
                new_reg_cir.save()
            return HttpResponseRedirect('/configuraciones/circuitos/')
    else:
        form_reg_cir = CircuitoForm()
    ctx = {'form_reg_cir': form_reg_cir, 'list_e': list_e, 'list_m': list_m}  # ctx = Contexto
    return render_to_response('circuito/circuito.html',
                              ctx, context_instance=RequestContext(request))


@login_required(login_url='/')
def EditarCircuito(request, pk):
    """ Vista basada en Metodos o funciones: (`Modificar`)."""
    obj_reg_cir = Circuito.objects.get(id=pk)
    list_e = Estado.objects.all()
    list_m = Municipio.objects.all()
    if request.method == 'POST':
        obj_reg_edit_cir = CircuitoForm(request.POST, request.FILES, instance=obj_reg_cir)
        if obj_reg_edit_cir.is_valid():
            new_reg_cir = obj_reg_edit_cir.save(commit=False)
            new_reg_cir.save()
            return HttpResponseRedirect('/configuraciones/circuitos/')
    else:
        obj_reg_edit_cir = CircuitoForm(instance=obj_reg_cir)
    ctx = {'obj_reg_edit_cir': obj_reg_edit_cir, 'obj_reg_cir': obj_reg_cir, 'list_e': list_e,
           'list_m': list_m}  # ctx = Contexto
    return render_to_response('circuito/modificar.html',
                              ctx, context_instance=RequestContext(request))


class ListarCircuito(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    
    """
    model = Circuito
    template_name = 'circuito/listar.html'
    context_object_name = "listar_circuito"


class BorrarCircuito(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
        satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Circuito
    template_name = 'circuito/borrar.html'
    context_object_name = "borrar_circuito"
    success_url = reverse_lazy("listar_circuito")
