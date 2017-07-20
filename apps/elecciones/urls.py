from django.conf.urls import patterns, include, url
from .views import RegistrarEleccion, ListarEleccion, BorrarEleccion, EditarEleccion, tipo_ajax
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion elecciones, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarEleccion.as_view(template_name="elecciones/listar.html"),
                                                 login_url='/'), name='listar_eleccion'),
                       url(r'^registrareleccion/', 'apps.elecciones.views.RegistrarEleccion',
                           name="registrar_eleccion",),
                       url(r'^editareleccion/(?P<pk>\d+)/$', 'apps.elecciones.views.EditarEleccion',
                           name="editar_eleccion",),
                       url(r'^borrareleccion/(?P<pk>\d+)/$', login_required(BorrarEleccion.as_view(template_name="elecciones/borrar.html"),
                                                                            login_url='/'), name='borrar_eleccion'),
                       url(r'^tipo_ajax/$', 'apps.elecciones.views.tipo_ajax', name='tipo_ajax',),

                       )
