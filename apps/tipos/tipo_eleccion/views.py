from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Tipo_eleccion
from .forms import Tipo_eleccionForm
from apps.tipos.categoria_eleccion.models import Categoria
from django.http import HttpResponseRedirect, HttpResponse
from apps.elecciones.models import Eleccion


class RegistrarTipo_eleccion(CreateView):
    """ Vista basada en clase: (`Registrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminado el registro
        satisfactoriamente
    :param form_class: nombre de la clase Formulario
    """
    template_name = 'tipos_eleccion/tipos.html'
    model = Tipo_eleccion
    success_url = reverse_lazy("listar_tipos")
    form_class = Tipo_eleccionForm

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(RegistrarTipo_eleccion, self).get_context_data(**kwargs)
        # Agregamos un QuerySet
        context['list_c'] = Categoria.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        bandera = request.POST.get('bandera')
        categoria = request.POST.get('categoria')
        tipo = request.POST.get('tipo')
        existe = Tipo_eleccion.objects.filter(categoria_id=categoria, tipo=tipo).exists()
        if existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/configuraciones/tipo_eleccion/tipos/')


class ListarTipo_eleccion(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    
    """
    model = Tipo_eleccion
    template_name = 'tipos_eleccion/listar.html'
    context_object_name = "listar_tipos"


class EditarTipo_eleccion(UpdateView):
    """ Vista basada en clase: (`Editar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminada la edicion del
        registro satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Tipo_eleccion
    template_name = 'tipos_eleccion/modificar.html'
    context_object_name = "editar_tipos"
    success_url = reverse_lazy("listar_tipos")

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(EditarTipo_eleccion, self).get_context_data(**kwargs)
        # Agregamos un QuerySet
        context['list_c'] = Categoria.objects.all()
        return context


class BorrarTipo_eleccion(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
                            satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Tipo_eleccion
    template_name = 'tipos_eleccion/borrar.html'
    context_object_name = "borrar_tipos"
    success_url = reverse_lazy("listar_tipos")

    def get_context_data(self, **kwargs):
        context = super(BorrarTipo_eleccion, self).get_context_data(**kwargs)
        id_tipo = self.kwargs['pk']
        ele = Eleccion.objects.all()
        existe = ele.filter(tipo_eleccion=id_tipo)
        cantidad = len(existe)

        context['cantidad'] = cantidad
        return context
