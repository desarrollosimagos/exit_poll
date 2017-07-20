# -*- coding: utf-8 -*-
from django.db import models
from apps.candidatos.models import Candidatos
from apps.elecciones.models import Eleccion
from apps.circuitos.models import Circuito
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from django.contrib.auth.models import User


class ExitPoll(models.Model):
    """ Clase que define todo lo referente a los Registros de asociación
    de canditados con Eleccion: Registrar, Modificar, Eliminar y Consultar

    :param ForeignKey eleccion: campo que llama al modelo Eleccion.
    :param ForeignKey candidatos: campo que llama al modelo Candidatos.
    :param ForeignKey estado: campo que llama al modelo Estados.
    :param IntegerField municipio: campo que a traves de ajax carga los municipios asociados a los estados.
    :param IntegerField parroquia: campo que a traves de ajax carga los parroquias asociados a los estados.
    :param IntegerField circuito: campo que a traves de ajax carga los circuitos asociados a los estados.
    :param IntegerField sectores: campo que a traves de ajax carga los sectores asociados a los estados.
    :param IntegerField poligonal: campo que a traves de ajax carga las poligonales asociados a los estados.
    :param IntegerField centro: campo que a traves de ajax carga los centros asociados a los estados.
    
    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    """
    eleccion = models.ForeignKey(Eleccion, null=True)
    candidatos = models.ForeignKey(Candidatos, null=True)
    estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='estado_exitpoll', null=True, blank=True)
    municipio = models.IntegerField(null=True, blank=True)
    parroquia = models.IntegerField(null=True, blank=True)
    circuito = models.IntegerField(null=True, blank=True)
    sector = models.IntegerField(null=True, blank=True)
    poligonal = models.IntegerField(null=True, blank=True)
    
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True,)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """
            :param unique_together: verifica que no existan candidatos repetidos en un mismo exit poll en base a la eleccion y el candidato
            :param ordering: Ordena los registros en base a el campo eleccion y candidatos
        """
        unique_together = ("eleccion", "candidatos")
        ordering = ('eleccion', 'candidatos', 'estado', 'municipio', 'circuito', 'sector', 'poligonal')

    #def __unicode__(self):
    #    """
    #        :returns: Representacion en cadena de la clase ExitPoll
    #    """
    #    return self.eleccion

    def get_absolute_url(self):
        """
            :returns: La Url de vista principal de administracion de ExitPoll
        """
        return ('listar_exitpoll', [self.id, ])