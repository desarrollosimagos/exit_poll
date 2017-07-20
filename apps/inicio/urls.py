from django.conf.urls import patterns, include, url
from .views import Inicio

"""
    Urls principal del sistema a la pagina de inicio
"""
urlpatterns = patterns('',
                       url(r'^$', Inicio.as_view()),
                       )
