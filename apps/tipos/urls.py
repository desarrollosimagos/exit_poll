from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^categorias/', include('apps.tipos.categoria_eleccion.urls')),
                       url(r'^tipos/', include('apps.tipos.tipo_eleccion.urls')),

                       )
