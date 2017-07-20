from django.conf.urls import patterns, include, url
from .views import RegistrarPregunta, EditarPregunta, BorrarPreguntas
#from .views import RegistrarPreguntas
#, BorrarEncuesta
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion Preguntas, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
"""
urlpatterns = patterns('',
                       #url(r'^$', login_required(ListarEncuesta.as_view(template_name="registro/encuesta/listar.html"),
                       #                          login_url='/'), name='listar_encuestaes'),
                       url(r'^registrarpreguntas/$', login_required(RegistrarPregunta.as_view(template_name="registro/encuesta/listar.html"),
                                                 login_url='/'), name='registrar_preguntas'),
                       #url(r'^registrarpreguntas/', login_required(RegistrarPregunta.as_view(),
                       #                         login_url='/'), name='registrar_preguntas'),
                       url(r'^editarpreguntas/(?P<pk>\d+)/$', login_required(EditarPregunta.as_view(template_name="registro/encuesta/modificar_pregunta.html"),
                                                 login_url='/'), name='editar_pregunta'),
                       url(r'^borrarpreguntas/$', login_required(BorrarPreguntas.as_view(),
                                                                             login_url='/'), name='borrar_pregunta'),
                       )
