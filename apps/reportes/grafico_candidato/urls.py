from django.conf.urls import patterns, include, url
from .views import GraficaCandidato, eleccion_candidato, ReporteCandidatoGrupo
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(GraficaCandidato.as_view(template_name="reportes/grafica_candidato.html"),login_url='/'), name='grafica'),
                       url(r'^eleccion_candidato/$', 'apps.reportes.grafico_candidato.views.eleccion_candidato', name='eleccion_candidato',),
                       url(r'^candidatogrupo/$', login_required(ReporteCandidatoGrupo.as_view(),login_url='/')),
                       )
