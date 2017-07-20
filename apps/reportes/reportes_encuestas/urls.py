from django.conf.urls import patterns, include, url
from .views import FiltroEncuestas, ReporteEncuesta
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       url(r'^$', login_required(FiltroEncuestas.as_view(), login_url='/'), name='reporte_encuestas'),
                       url(r'^reporte_encuesta/(?P<id>\d+)$', login_required(ReporteEncuesta.as_view(),
                                                login_url='/'), name='reporte_encuesta'),
                       )
