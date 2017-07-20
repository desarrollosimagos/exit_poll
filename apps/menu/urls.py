from django.conf.urls import patterns, include, url
from .views import Inicio, PrincipalEncuesta, PrincipalExit
from django.contrib.auth.decorators import login_required


"""
    Urls a la plantilla base de la aplicacion
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(Inicio.as_view(template_name="inicio.html"), login_url='/')),
                       url(r'^sistema_encuestas$', login_required(PrincipalEncuesta.as_view(), login_url='/')),
                       url(r'^exit_polls$', login_required(PrincipalExit.as_view(), login_url='/')),
                       url(r'^/', include('apps.configuraciones.urls')),

                       )
