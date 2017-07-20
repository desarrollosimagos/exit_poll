from django.conf.urls import patterns, include, url
#from apps.configuraciones.views import Configuraciones

urlpatterns = patterns('',
                       #url(r'^$', include('apps.inicio.urls')),
                       url(r'^', include('apps.login.urls')),
                       url(r'^menu/', include('apps.menu.urls')),
                       url(r'^configuraciones/', include('apps.configuraciones.urls')),
                       url(r'^partidos/', include('apps.partidos.urls')),
                       url(r'^elecciones/', include('apps.elecciones.urls')),
                       url(r'^exitpoll/', include('apps.exitpoll.urls')),
                       url(r'^candidatos/', include('apps.candidatos.urls')),
                       url(r'^reportes/', include('apps.reportes.urls')),
                       url(r'^encuestas/', include('apps.registro.encuestas.urls')),
                       url(r'^preguntas/', include('apps.registro.preguntas.urls')),
                       url(r'^respuestas/', include('apps.registro.respuestas.urls')),
                       url(r'^aplicada/', include('apps.aplicada.urls')),
                       )
