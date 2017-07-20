from django.conf.urls import patterns, include, url
from .views import ListarFiltros, ReporteExitPollsCandidatos, ReporteDetallado, ReporteCandidatoBasico, ReporteCandidatoDetallado
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarFiltros.as_view(template_name="reportes/detallados.html"),login_url='/'), name='detallados'),
                       url(r'^exit_candidatos/(?P<from_date>[0-9]{2}\-[0-9]{2}\-[0-9]{4})/(?P<to_date>[0-9]{2}\-[0-9]{2}\-[0-9]{4})$', login_required(ReporteExitPollsCandidatos.as_view(),login_url='/')),
                       url(r'^detallado/(?P<from_date>[0-9]{2}\-[0-9]{2}\-[0-9]{4})/(?P<to_date>[0-9]{2}\-[0-9]{2}\-[0-9]{4})$', login_required(ReporteDetallado.as_view(),login_url='/')),
                       url(r'^candidato/(?P<candidato>\d+)$', login_required(ReporteCandidatoBasico.as_view(),login_url='/')),
                       url(r'^candidato_detallado/(?P<candidato>\d+)$', login_required(ReporteCandidatoDetallado.as_view(),login_url='/')),
                       )
