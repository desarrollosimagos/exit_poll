# -*- coding: utf-8 -*-
'''Modelo para el Registro de Grupos Etáreos'''
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Grupo_Etareo(models.Model):
    """ Clase que define todo lo referente a los `Partidos`:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField descripcion: campo para la descripcion del grupo etareo.
    :param CharField grupo_etareo: campo para colocar el rango de edades.
    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.

    """
    descripcion = models.CharField(max_length=20, verbose_name="Descripción", unique=True, null=True)
    desde = models.CharField(max_length=2, verbose_name="Desde", null=True, blank=True)
    hasta = models.CharField(max_length=2, verbose_name="Hasta", null=True, blank=True)

    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """
        :param ordering: Ordena los registros en base a el campo grupo_etareo
        """
        ordering = ('descripcion',)

    def __unicode__(self):
        return self.descripcion

    def get_absolute_url(self):
        return ('listar_grupo_etareo', [self.id, ])
