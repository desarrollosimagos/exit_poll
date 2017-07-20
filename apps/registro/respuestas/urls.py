from django.conf.urls import patterns, include, url
from .views import RegistrarRespuestas, EditarRespuestas, BorrarRespuestas

from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion Preguntas, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',

                       url(r'^registrarrespuestas/$', login_required(RegistrarRespuestas.as_view(template_name="registro/encuesta/listar.html"),
                                                 login_url='/'), name='registrar_respuestas'),
                       url(r'^editarrespuestas/(?P<pk>\d+)/$', login_required(EditarRespuestas.as_view(template_name="registro/encuesta/modificar_respuesta.html"),
                                                 login_url='/'), name='editar_respuestas'),
                       url(r'^borrarrespuestas/$', login_required(BorrarRespuestas.as_view(),
                                                                             login_url='/'), name='borrar_respuesta'),


                       )
