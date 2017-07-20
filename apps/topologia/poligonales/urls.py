from django.conf.urls import patterns, include, url
from .views import ListarPoligonal, BuscarAjaxSector, BorrarPoligonal
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion Poligonales, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarPoligonal.as_view(template_name="topologia/poligonales/listar.html"),
                                                 login_url='/'), name='listar_poligonales'),
                       url(r'^registrarpoligonal/', 'apps.topologia.poligonales.views.RegistrarPoligonal',
                           name="registrar_poligonal",),
                       url(r'^editarpoligonal/(?P<pk>\d+)/$', 'apps.topologia.poligonales.views.ActualizarPoligonal',
                           name='editar_poligonal',),
                       url(r'^borrarpoligonal/(?P<pk>\d+)/$', login_required(BorrarPoligonal.as_view(template_name="topologia/poligonales/borrar.html"),
                                                                           login_url='/'), name='borrar_poligonal'),
                       url(r'^busqueda_sector/$', 'apps.topologia.poligonales.views.BuscarAjaxSector',
                           name='busqueda_sector'),

                       )
