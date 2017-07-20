# -*- coding: utf-8 -*-
'''Modelo para el Registro Poligonales'''
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    ('1', "Borrador"),
    ('2', "Finalizada"),
    ('3', "Cerrada"),
)
TIPO = (
    ('1', "Web"),
    ('2', "Móvil"),
    ('3', "Web y Móvil"),
)


class Encuesta(models.Model):
    """ Clase que define todo lo referente a las 'Encuesta':
    Registrar, Modificar, Eliminar y Consultar

    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    """

    cod_encuesta = models.IntegerField(verbose_name="Código de Encuesta", max_length=4)
    nombre = models.CharField(verbose_name="Nombre de la Encuesta", max_length=150)
    estatus = models.CharField(choices=STATUS, default=1, max_length=2)
    tipo = models.CharField(choices=TIPO, max_length=2, null=True, blank=True)
    tipo_aplicacion = models.IntegerField(null=True)

    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """
        :param unique_together: verifica que no existan centros repetidos en base a su nombre codigo estado
            municipio y parroquia
        :param ordering: Ordena los registros en base a el campo cod_n nombre estado
        """
        unique_together = ("cod_encuesta", "nombre")
        #ordering = ('cod_encuesta')

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return ('listar_encuesta', [self.id, Encuesta])
