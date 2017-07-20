# -*- coding: utf-8 -*-
from django.db import models
from apps.exitpoll.models import ExitPoll
from apps.grupo_etareo.models import Grupo_Etareo
from apps.candidatos.models import Candidatos
from apps.elecciones.models import Eleccion
# from apps.topologia.estados.models import Estado
# from apps.topologia.municipios.models import Municipio
# from apps.circuitos.models import Circuito
from django.contrib.auth.models import User

SEXO = (
    ('1', "Femenino"),
    ('2', "Masculino"),
)


class Votacion(models.Model):
    '''Registro de Votos'''
    grupo_etareo = models.IntegerField(max_length=2)
    candidatos = models.ForeignKey(Candidatos)
    eleccion = models.ForeignKey(Eleccion, null=True)
    sexo = models.CharField(choices=SEXO, default=0, max_length=15)
    estado = models.IntegerField(max_length=3, null=True, blank=True)
    circuito = models.IntegerField(max_length=3, null=True, blank=True)
    municipio = models.IntegerField(max_length=3, null=True, blank=True)
    parroquia = models.IntegerField(max_length=3, null=True, blank=True)
    sector = models.IntegerField(max_length=3, null=True, blank=True)
    poligonal = models.IntegerField(max_length=3, null=True, blank=True)
