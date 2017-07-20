# -*- coding: utf-8 -*-
'''Modelo para el Registro Poligonales'''
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.topologia.sectores.models import Sector
from django.contrib.auth.models import User


class Poligonal(models.Model):
    """ Clase que define todo lo referente a las `Centros`:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField poligonal: campo donde registra el nombre del poligonal.
    :param ForeignKey estado: campo que llama al modelo Estado.
    :param IntegerField municipio: campo que a traves de ajax carga los municipios asociados al estado.
    :param IntegerField parroquia: campo que a traves de ajax carga las parroquia asociados a los municipios.
    :param CharField cod_pol: campo para colocar el codigo del poligonal.
    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    """

    cod_pol = models.IntegerField(verbose_name="Código de la Poligonal", max_length=2)
    poligonal = models.CharField(verbose_name="Nombre de la Poligonal", max_length=150)
    estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL,
                               related_name='estado_poligonal', null=True)
    municipio = models.IntegerField(null=True)
    parroquia = models.IntegerField(null=True)
    sector = models.IntegerField(null=True)
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """
        :param unique_together: verifica que no existan centros repetidos en base a su nombre codigo estado
            municipio y parroquia
        :param ordering: Ordena los registros en base a el campo cod_n nombre estado
        """
        #unique_together = ("cod_pol", "poligonal", "estado")
        ordering = ('estado', 'municipio', 'parroquia', 'cod_pol')

    def __unicode__(self):
        return self.poligonal

    def get_absolute_url(self):
        return ('listar_poligonal', [self.id, Poligonal])
