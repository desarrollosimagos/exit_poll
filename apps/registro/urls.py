from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^encuestas/', include('apps.registros.encuestas.urls')),
                       url(r'^preguntas/', include('apps.registros.preguntas.urls')),
                       url(r'^respuestas/', include('apps.registros.respuestas.urls')),
                       )
