from django.conf.urls import patterns, include, url
from .views import ListarEncuesta, RegistrarEncuesta, BorrarEncuesta, FinalizarEncuesta, VerEncuesta, CerrarEncuesta
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion Encuesta, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarEncuesta.as_view(template_name="registro/encuesta/listar.html"),
                                                 login_url='/'), name='listar_encuestas'),
                       url(r'^registrarencuesta/', 'apps.registro.encuestas.views.RegistrarEncuesta',
                           name="registrar_encuesta",),
                       url(r'^editarencuesta/(?P<pk>\d+)/$', 'apps.registro.encuestas.views.EditarEncuesta',
                           name='editar_encuesta',),
                       url(r'^borrarencuesta/$', login_required(BorrarEncuesta.as_view(),
                                                login_url='/'), name='borrar_encuesta'),
                       url(r'^finalizar/$', login_required(FinalizarEncuesta.as_view(),
                                                login_url='/'), name='finalizar_encuesta'),
                       url(r'^cerrar/$', login_required(CerrarEncuesta.as_view(),
                                                login_url='/'), name='cerrar_encuesta'),
                       url(r'^verencuesta/(?P<encuesta>\d+)$', login_required(VerEncuesta.as_view(),
                                                login_url='/'), name='ver_encuesta'),

                       )