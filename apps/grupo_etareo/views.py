from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Grupo_Etareo
from apps.grupo_etareo.forms import Grupo_EtareoForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse
from apps.votacion.models import Votacion


class RegistrarGrupo_Etareo(CreateView):
    """ Vista basada en clase: (`Registrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminado el registro
        satisfactoriamente
    :param form_class: nombre de la clase Formulario
    """
    template_name = 'grupo_etareo/grupo_etareo.html'
    model = Grupo_Etareo
    success_url = reverse_lazy("listar_grupo_etareo")
    form_class = Grupo_EtareoForm

    def post(self, request, *args, **kwargs):
        bandera = request.POST.get('bandera')
        descripcion = request.POST.get('descripcion')
        desde = request.POST.get('desde')
        hasta = request.POST.get('hasta')
        existe_t = Grupo_Etareo.objects.filter(descripcion=descripcion, desde=desde, hasta=hasta).exists()
        existe_d = Grupo_Etareo.objects.filter(descripcion=descripcion).exists()
        existe_g = Grupo_Etareo.objects.filter(desde=desde, hasta=hasta).exists()
        if existe_t and bandera == 'true':
            return HttpResponse('existe_t')
        elif existe_d and bandera == 'true':
            return HttpResponse('existe_d')
        elif existe_g and bandera == 'true':
            return HttpResponse('existe_g')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/configuraciones/grupo_etareo/')


class ListarGrupo_Etareo(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Grupo_Etareo
    template_name = 'grupo_etareo/listar.html'
    context_object_name = "listar_grupo_etareo"


class EditarGrupo_Etareo(UpdateView):
    """ Vista basada en clase: (`Editar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminada la edicion del
        registro satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Grupo_Etareo
    template_name = 'grupo_etareo/modificar.html'
    context_object_name = "editar_grupo_etareo"
    success_url = reverse_lazy("listar_grupo_etareo")


class BorrarGrupo_Etareo(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
        satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Grupo_Etareo
    template_name = 'grupo_etareo/borrar.html'
    context_object_name = "borrar_grupo_etareo"
    success_url = reverse_lazy("listar_grupo_etareo")

