# -*- coding: utf-8 -*-
'''Modelo para el Registro Poligonales'''
from django.db import models
from django.contrib.auth.models import User
from apps.registro.preguntas.models import Preguntas

TIPO = (
    ('1', "Cerrada"),
    ('2', "Abierta"),
)


class Respuestas(models.Model):
    """ Clase que define todo lo referente a las 'Respuestas':
    Registrar, Modificar, Eliminar y Consultar

    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    """

    cod_pregunta = models.ForeignKey(Preguntas)
    cod_respuesta = models.IntegerField(verbose_name="Código de Respuestas", max_length=4)
    respuesta = models.CharField(verbose_name="Descripcion de la Respuestas", max_length=200)
    tipo = models.CharField(choices=TIPO, default=1, max_length=2)

    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateField(auto_now_add=False, auto_now=True, null=True)

    class Meta:

        unique_together = ("cod_pregunta","cod_respuesta", "respuesta")
 

    def __unicode__(self):
        return self.respuesta

    def get_absolute_url(self):
        return ('listar_respuesta', [self.id, Respuestas])
