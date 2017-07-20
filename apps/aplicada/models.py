# -*- coding: utf-8 -*-
from django.db import models

SEXO = (
    ('1', "Femenino"),
    ('2', "Masculino"),
)


class EncuestaResultado(models.Model):
    '''Registro de Votos'''
    cod_respuesta = models.IntegerField(verbose_name="Código Respuesta")
    otras = models.CharField(verbose_name="Otras", max_length=150, null=True, blank=True)
    cod_encuesta = models.IntegerField(verbose_name="Código Encuesta", null=True, blank=True)
    num_encuestado = models.IntegerField(verbose_name="Número de Encuestados", null=True, blank=True)
    grupo_etareo = models.IntegerField(max_length=2, null=True, blank=True)
    sexo = models.CharField(choices=SEXO, default=0, max_length=15, null=True, blank=True)
    estado = models.IntegerField(max_length=3, null=True, blank=True)
    municipio = models.IntegerField(max_length=3, null=True, blank=True)
