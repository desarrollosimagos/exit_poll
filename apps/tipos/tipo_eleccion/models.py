#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelos Para tipos de Elecciones'''
from django.db import models
from django.core.urlresolvers import reverse
from apps.tipos.categoria_eleccion.models import Categoria
from django.contrib.auth.models import User


class Tipo_eleccion(models.Model):
    """ Clase que define todo lo referente a las `Tipo_eleccion` en base a la categoria:
    Registrar, Modificar, Eliminar y Consultar

    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param IntegerField niveles: campo para seleccionar el nivel de la eleccion.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    :param ForeignKey categoria: campo que llama al modelo categoria.
    :param CharField categoria: campo donde registran las categorias.
    """
    categoria = models.ForeignKey(Categoria)  # Categoria Padre
    tipo = models.CharField(max_length=100, )  # Sub-tipo o sub-categoria
    niveles = models.IntegerField(null=True)
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """
        :param unique_together: atributo que valida que no el tipo de categoria sea unica por categoria
        :param ordering: Ordena los registros en base a el campo categoria y sus tipo
        """
        unique_together = ("categoria", "tipo")  # tipo unico por categoria seleccionada
        ordering = ('categoria', 'tipo')

    def __unicode__(self):
        return self.tipo

    def get_absolute_url(self):
        return ('listar_tipos', [self.id, ])
