from django.conf.urls import patterns, include, url
from .views import ListarSector, BorrarSector
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion centro_votacion, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarSector.as_view(template_name="topologia/sectores/listar.html"),
                                                 login_url='/'), name='listar_sectores'),
                       url(r'^registrarsector/', 'apps.topologia.sectores.views.RegistrarSector',
                           name="registrar_sector",),
                       url(r'^editarsector/(?P<pk>\d+)/$', 'apps.topologia.sectores.views.ActualizarSector',
                           name='editar_sector',),
                       url(r'^borrarsector/(?P<pk>\d+)/$', login_required(BorrarSector.as_view(template_name="topologia/sectores/borrar.html"),
                                                                           login_url='/'), name='borrar_sector'),

                       )
