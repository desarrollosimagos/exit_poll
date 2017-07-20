from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Votacion
from apps.candidatos.models import Candidatos
from apps.exitpoll.models import ExitPoll
from apps.elecciones.models import Eleccion
from django.core import serializers
from apps.grupo_etareo.models import Grupo_Etareo
from apps.partidos.models import Partidos


class RegistrarVotacion(CreateView):
    template_name = 'votacion/votar.html'
    model = Votacion
    fields = ['grupo_etareo', 'sexo', 'candidatos', 'eleccion', 'estado', 'circuito', 'municipio']
    success_url = reverse_lazy("menumovil")

    def get_context_data(self, **kwargs):
        id_can = self.kwargs['pk']
        id_elec = self.kwargs['idele']

        context = super(RegistrarVotacion, self).get_context_data(**kwargs)
        candi = Candidatos.objects.all()
        candi = candi.filter(pk=id_can)
        id_partido = candi.values('part_politico_id')
        
        foto_par = Partidos.objects.filter(id=id_partido).values('foto_partido')
        print "HOLA",foto_par
        id_grupo = self.kwargs['grupo']
        id_sexo = self.kwargs['sexo']
        id_estado = self.kwargs['estado']
        id_circuito = self.kwargs['circuito']
        id_municipio = self.kwargs['municipio']

        
        context['id_elec'] = id_elec
        context['listar_candidato'] = candi.values('nombre', 'apellido', 'foto', 'id')
        context['id_sexo'] = id_sexo
        context['id_grupo'] = id_grupo
        context['id_estado'] = id_estado
        context['id_circuito'] = id_circuito
        context['id_municipio'] = id_municipio
        context['foto_par'] = foto_par
        return context


class ListarVotacion(ListView):
    
    model = Votacion
    template_name = 'votacion/listar1.html'
    context_object_name = "listar_votacion"


from django.db.models import Count


#Combo de Lista de Elecciones Activas y No Activas
class ListarVotos(ListView):
    model = Votacion
    template_name = 'votacion/filtro.html'

    def get_context_data(self, **kwargs):
        context = super(ListarVotos, self).get_context_data(**kwargs)
        listar = Eleccion.objects.all()
        context['listar'] = listar
        return context


#Listado de Totales de Elecciones
class Listado(ListView):
    model = Votacion
    template_name = 'votacion/cantidad_votos.html'

    def get_context_data(self, **kwargs):
        id_ele = self.kwargs['pk']
        context = super(Listado, self).get_context_data(**kwargs)
        listar_elecciones = Eleccion.objects.get(id=id_ele)
        listar = ExitPoll.objects.filter(eleccion_id=id_ele)
        cand_id = listar.values('candidatos_id')
        queryset = Votacion.objects.filter(candidatos_id=cand_id, eleccion_id=id_ele).values('candidatos_id', 'candidatos__nombre', 'candidatos__apellido', 'candidatos__foto').annotate(total=Count('candidatos_id'))

        context['queryset'] = queryset
        context['listar_elecciones'] = listar_elecciones.nombre
        return context
