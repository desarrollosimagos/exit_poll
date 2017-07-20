#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelos Para Categorias de Elecciones'''
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Categoria(models.Model):
    """ Clase que define todo lo referente a la `Categoria de eleccion`:
    Registrar, Modificar, Eliminar y Consultar

    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    :param CharField categoria: campo donde registran las categorias.
    """
    categoria = models.CharField(max_length=50, unique=True)
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """
        :param ordering: Ordena los registros en base a el campo categoria
        """
        ordering = ('categoria', )

    def __unicode__(self):
        return self.categoria

    def get_absolute_url(self):
        return ('listar_categoria', [self.id, ])
