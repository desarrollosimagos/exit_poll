# -*- coding: utf-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.tipos.categoria_eleccion.models import Categoria
from apps.tipos.tipo_eleccion.models import Tipo_eleccion
import datetime
from django.contrib.auth.models import User


class Eleccion(models.Model):
    """ Clase que define todo lo referente a la Informacion del proceso `Electoral`:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField nombre: El nombre del proceso Electoral
    :param ForeignKey categoria_eleccion: La categoria que abarca la eleccion
    :param IntegerField tipo_eleccion: Tipo de eleccion segun la categoria que seleccione

    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    """
    #Informacion Principal
    nombre = models.CharField(verbose_name="Nombre del Proceso Electoral", max_length=100)
    categoria_eleccion = models.ForeignKey(Categoria)
    tipo_eleccion = models.IntegerField(null=True)
    ele_activa = models.BooleanField(default=False)
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        unique_together = ("nombre",)
        ordering = ('nombre',)

    def __unicode__(self):
        #return: Representacion en cadena de la clase Partidos
        return self.nombre

    def get_absolute_url(self):
        return ('listar_eleccion', [self.id, ])
