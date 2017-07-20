# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import os


def generate_new_filename(instance, filename):
    f, ext = os.path.splitext(filename)
    return '%s%s' % ('logo_partidos/'+str(instance.siglas), ext)


class Partidos(models.Model):
    """ Clase que define todo lo referente a los Partidos:
        Registrar, Modificar, Eliminar y Consultar

        :param CharField n_partidos: campo donde registra el nombre del centro.
        :param CharField siglas: campo para colocar las siglas del partido.
        :param ImageField foto_partido: campo de tipo imagen para guardar el logo del partido.
        :param CharField nom_presidente: campo donde registra el nombre del presidente del partido
        :param CharField ape_presidente: campo donde registra el apellido del presidente del partido
        :param CharField correo: campo para ingresar el correo del partido
        :param CharField twitter: campo para ingresar el twitter del partido
        :param CharField telefono: campo donde ingresamos el telefono del partido.
        :param ForeignKey user_create: campo que llama al modelo User.
        :param ForeignKey user_update: campo que llama al modelo User.
        :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
        :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.

    """

    n_partidos = models.CharField(verbose_name="Nombre del Partido",  max_length=150, unique=True)
    siglas = models.CharField(max_length=10, unique=True)
    foto_partido = models.ImageField(upload_to=generate_new_filename)
    nom_presidente = models.CharField(verbose_name="Nombre del Presidente", max_length=100, unique=True)
    ape_presidente = models.CharField(verbose_name="Apellido del Presidente", max_length=100, unique=True)
    correo = models.EmailField(max_length=200, unique=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=11, verbose_name="Teléfono", unique=True)
    partido_binario = models.TextField(null=True, blank=True)

    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """
            :param unique_together: verifica que no se registren partidos con el mismo nombre y siglas
            :param ordering: Ordena los registros en base a el campo n_partidos
        """
        unique_together = ("n_partidos", "siglas")
        ordering = ('n_partidos',)

    def __unicode__(self):
        """
            :returns: Representacion en cadena de la clase partidos
        """
        return self.siglas

    def get_absolute_url(self):
        """
            :returns: La Url de vista principal de administracion de Partidos
        """
        return ('listar_partido', [self.id, ])
