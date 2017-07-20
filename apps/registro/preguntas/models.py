# -*- coding: utf-8 -*-
'''Modelo para el Registro Poligonales'''
from django.db import models
from django.contrib.auth.models import User

TIPO = (
    ('1', "Excluyente"),
    ('2', "No Excluyente"),
)


class Preguntas(models.Model):
    """ Clase que define todo lo referente a las 'Preguntas':
    Registrar, Modificar, Eliminar y Consultar

    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    """

    cod_encuesta = models.IntegerField(verbose_name="Código de Encuesta", max_length=4)
    cod_pregunta = models.IntegerField(verbose_name="Código de Pregunta", max_length=4)
    pregunta = models.CharField(verbose_name="Descripcion de la Pregunta", max_length=300)
    tipo = models.CharField(choices=TIPO, default=1, max_length=2)

    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateField(auto_now_add=False, auto_now=True, null=True)

    class Meta:

        unique_together = ("cod_pregunta", "pregunta")
 

    def __unicode__(self):
        return self.pregunta

    def get_absolute_url(self):
        return ('listar_preguntas', [self.id, Preguntas])
