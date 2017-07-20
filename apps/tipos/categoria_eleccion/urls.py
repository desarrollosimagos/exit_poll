from django.conf.urls import patterns, include, url
from .views import RegistrarCategoria, ListarCategoria, BorrarCategoria, EditarCategoria
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion categoria_eleccion, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarCategoria.as_view(template_name="categoria_eleccion/listar.html"),
                                                 login_url='/'), name='listar_categoria'),
                       url(r'^registrarcategoria/$', login_required(RegistrarCategoria.as_view(template_name="categoria_eleccion/categoria.html"),
                                                 login_url='/'), name='registrar_categoria'),
                       url(r'^editarcategoria/(?P<pk>\d+)/$',login_required(EditarCategoria.as_view(template_name="categoria_eleccion/modificar.html"),
                                                 login_url='/'), name='editar_categoria'),
                       url(r'^borrarcategoria/(?P<pk>\d+)/$', login_required(BorrarCategoria.as_view(template_name="categoria_eleccion/borrar.html"),
                                                 login_url='/'), name='borrar_categoria'),

                       )
