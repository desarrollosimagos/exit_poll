from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^graficas/', include('apps.reportes.reportes.urls')),
                       url(r'^reportes_detallados/', include('apps.reportes.reportes_detallados.urls')),
                       url(r'^graficas_candidatos/', include('apps.reportes.grafico_candidato.urls')),
                       url(r'^encuestas/', include('apps.reportes.reportes_encuestas.urls')),
                       )
