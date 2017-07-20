from django.conf.urls import patterns, include, url
from .views import RegistrarCircuito, ListarCircuito, BorrarCircuito, EditarCircuito
from django.contrib.auth.decorators import login_required

"""
    Urls para ingresar a la aplicacion circuitos, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarCircuito.as_view(template_name="circuito/listar.html"),
                                                 login_url='/'), name='listar_circuito'),
                       url(r'^registrarcircuito/', 'apps.circuitos.views.RegistrarCircuito',
                           name="registrar_circuito",),
                       url(r'^editarcircuito/(?P<pk>\d+)/$', 'apps.circuitos.views.EditarCircuito',
                           name="editar_circuito",),
                       url(r'^borrarcircuito/(?P<pk>\d+)/$', login_required(BorrarCircuito.as_view(template_name="circuito/borrar.html"),
                                                 login_url='/'), name='borrar_circuito'),
                       )
