from django.conf.urls import patterns, include, url
from .views import RegistrarPartidos, ListarPartidos, BorrarPartidos, EditarPartidos
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion partidos, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarPartidos.as_view(template_name="partido/listar.html"),
                                                 login_url='/'), name='listar_partido'),
                       url(r'^registrarpartido/$', 'apps.partidos.views.RegistrarPartidos',
                           name='registrar_partido'),
                       url(r'^editarpartido/(?P<pk>\d+)/$', 'apps.partidos.views.EditarPartidos',
                           name='editar_partido',),
                       url(r'^borrarpartido/(?P<pk>\d+)/$', login_required(BorrarPartidos.as_view(template_name="partido/borrar.html"),
                                                 login_url='/'), name='borrar_partido'),

                       )
