from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^estados/', include('apps.topologia.estados.urls')),
                       url(r'^municipios/', include('apps.topologia.municipios.urls')),
                       url(r'^parroquias/', include('apps.topologia.parroquias.urls')),
                       url(r'^sectores/', include('apps.topologia.sectores.urls')),
                       url(r'^poligonales/', include('apps.topologia.poligonales.urls')),
                       )
