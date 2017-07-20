from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Categoria
from django.views.generic.edit import FormView
from apps.tipos.categoria_eleccion.forms import CategoriaForm
from django.http import HttpResponseRedirect, HttpResponse
from apps.tipos.tipo_eleccion.models import Tipo_eleccion


class RegistrarCategoria(CreateView):
    """ Vista basada en clase: (`Registrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminado el registro
        satisfactoriamente
    :param form_class: nombre de la clase Formulario
    """
    template_name = 'categoria_eleccion/categoria.html'
    model = Categoria
    success_url = reverse_lazy("listar_categoria")
    form_class = CategoriaForm

    def post(self, request, *args, **kwargs):
        bandera = request.POST.get('bandera')
        categoria = request.POST.get('categoria')
        existe = Categoria.objects.filter(categoria=categoria).exists()
        if existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/configuraciones/tipo_eleccion/categorias/')


class ListarCategoria(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    
    """
    model = Categoria
    template_name = 'categoria_eleccion/listar.html'
    context_object_name = "listar_categoria"


class EditarCategoria(UpdateView):
    """ Vista basada en clase: (`Editar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminada la edicion del registro satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Categoria
    template_name = 'categoria_eleccion/modificar.html'
    context_object_name = "editar_categoria"
    success_url = reverse_lazy("listar_categoria")


class BorrarCategoria(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
                            satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Categoria
    template_name = 'categoria_eleccion/borrar.html'
    context_object_name = "borrar_categoria"
    success_url = reverse_lazy("listar_categoria")

    def get_context_data(self, **kwargs):
        context = super(BorrarCategoria, self).get_context_data(**kwargs)
        id_cat = self.kwargs['pk']
        tipo = Tipo_eleccion.objects.all()
        existe = tipo.filter(categoria_id=id_cat)
        cantidad = len(existe)

        context['cantidad'] = cantidad
        return context
