from django.conf.urls import patterns, url
from .views import RegistrarExitPoll, ListarExitPoll, BorrarExitPoll, ListarCandidatos, MenuMovil
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion exitpoll, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', ListarExitPoll.as_view(), name='listar_exitpoll'),
                       url(r'^registrarexitpoll/$', login_required(RegistrarExitPoll.as_view()), name='registrar_exitpoll'),
                       #url(r'^editarexitpoll/(?P<pk>\d+)/$', EditarExitPoll.as_view(), name='editar_exitpoll'),
                       url(r'^borrarexitpoll/(?P<pk>\d+)/$', login_required(BorrarExitPoll.as_view()), name='borrar_exitpoll'),
                       url(r'^listarcandidato/(?P<pk>\d+)/(?P<grupo>\d+)/(?P<sexo>\d+)/(?P<estado>\d+)/(?P<circuito>\d+)/(?P<municipio>\d+)/$', ListarCandidatos.as_view(), name='candidatos'),
                       url(r'^menumovil/$', MenuMovil.as_view(), name='menumovil'),
                       url(r'^exit_poll_ajax/$', 'apps.exitpoll.views.exit_poll_ajax', name='exitpoll_ajax'),
                       #url(r'^busqueda_poligonal/$', 'apps.exitpoll.views.BuscarAjaxPoligonal', name='busqueda_poligonal'),
                       )