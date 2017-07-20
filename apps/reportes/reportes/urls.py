from django.conf.urls import patterns, include, url
from .views import ListarGrafica, ReporteCandidato, ReporteGrupo, ReporteDetallado, ReporteSexo
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarGrafica.as_view(template_name="reportes/grafica.html"),login_url='/'), name='grafica'),
                       url(r'^exitpoll/$', login_required(ReporteCandidato.as_view(),login_url='/')),
                       url(r'^exitpollgrupo/$', login_required(ReporteGrupo.as_view(),login_url='/')),
                       url(r'^exitpolldetallado/$', login_required(ReporteDetallado.as_view(),login_url='/')),
                       url(r'^exitpollgenero/$', login_required(ReporteSexo.as_view(),login_url='/')),
                       )
