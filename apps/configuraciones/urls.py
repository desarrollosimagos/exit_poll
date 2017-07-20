from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a los diferentes menus que estan en configuraciones
"""
urlpatterns = patterns('',
                       url(r'^topologia/', include('apps.topologia.urls')),
                       url(r'^circuitos/', include('apps.circuitos.urls')),
                       url(r'^grupo_etareo/', include('apps.grupo_etareo.urls')),
                       url(r'^tipo_eleccion/', include('apps.tipos.urls')),
                       )
