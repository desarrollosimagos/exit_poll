from django.conf.urls import patterns, include, url
from .views import ListarVotacion, RegistrarVotacion, ListarVotos, Listado

urlpatterns = patterns('',
                       #url(r'^listarcandidato/$', ListarVotacion.as_view(), name='listar_votacion'),
                       url(r'^votar/(?P<pk>\d+)/(?P<idele>\d+)/(?P<grupo>\d+)/(?P<sexo>\d+)/(?P<estado>\d+)/(?P<circuito>\d+)/(?P<municipio>\d+)/$', RegistrarVotacion.as_view(), name='votar'),
                       url(r'^consulta/$', ListarVotos.as_view(), name='votos'),
                       url(r'^listar_resultados/(?P<pk>\d+)$', Listado.as_view(), name='listar_resultados'),
                       )
