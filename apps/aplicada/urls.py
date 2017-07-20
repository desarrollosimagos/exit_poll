# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import GuardarEncuestas, EncuestaWebView, EncuestaWeb


urlpatterns = patterns('',
                       url(r'^guardar_encuesta/$', GuardarEncuestas.as_view(),
                           name='guardar_encuesta'),
                       url(r'^encuesta_web/(?P<cod_pregunta>.+)/$',
                           EncuestaWeb.as_view(), name='encuesta_web'),
                       url(r'^encuesta_api/(?P<cod_pregunta>.+)/$',
                           EncuestaWebView.as_view(), name='buscar'),
                       )