from django.conf.urls import patterns, include, url
from .views import RegistrarCandidatos, ListarCandidatos, BorrarCandidatos, EditarCandidatos
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion candidatos, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarCandidatos.as_view(template_name="candidato/listar.html"),
                                                 login_url='/'), name='listar_candidato'),
                       url(r'^registrarcandidato/', 'apps.candidatos.views.RegistrarCandidatos',
                           name="registrar_candidato",),
                       url(r'^editarcandidato/(?P<pk>\d+)/$', 'apps.candidatos.views.EditarCandidatos',
                           name="editar_candidato",),
                       url(r'^borrarcandidato/(?P<pk>\d+)/$', login_required(BorrarCandidatos.as_view(template_name="candidato/borrar.html"),
                                                                             login_url='/'), name='borrar_candidato'),
                       #url(r'^nivel_ajax/$', 'apps.candidatos.views.nivel_ajax', name='ajax_candidato',),
                       )
