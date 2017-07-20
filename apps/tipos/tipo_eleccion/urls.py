from django.conf.urls import patterns, include, url
from .views import RegistrarTipo_eleccion, ListarTipo_eleccion, BorrarTipo_eleccion, EditarTipo_eleccion
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion tipo_eleccion, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
    y ruta a metodos con ajax.
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarTipo_eleccion.as_view(template_name="tipos_eleccion/listar.html"),
                                                 login_url='/'), name='listar_tipos'),
                       url(r'^registrartipos/$', login_required(RegistrarTipo_eleccion.as_view(template_name="tipos_eleccion/tipos.html"),
                                                 login_url='/'), name='registrar_tipos'),
                       url(r'^editartipos/(?P<pk>\d+)/$', login_required(EditarTipo_eleccion.as_view(template_name="tipos_eleccion/modificar.html"),
                                                 login_url='/'), name='editar_tipos'),
                       url(r'^borrartipos/(?P<pk>\d+)/$', login_required(BorrarTipo_eleccion.as_view(template_name="tipos_eleccion/borrar.html"),
                                                 login_url='/'), name='borrar_tipos'),

                       )
