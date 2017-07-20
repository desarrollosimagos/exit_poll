# -*- coding: utf-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.tipos.categoria_eleccion.models import Categoria
from apps.tipos.tipo_eleccion.models import Tipo_eleccion
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.partidos.models import Partidos
from apps.elecciones.models import Eleccion
from apps.circuitos.models import Circuito
from django.contrib.auth.models import User
import os

#Diccionario
SEXO = (
    ('1', "Femenino"),
    ('2', "Masculino"),
)


def generate_new_filename(instance, filename):
    f, ext = os.path.splitext(filename)
    return '%s%s' % ('foto_candidato/'+str(instance.cedula), ext)


class Candidatos(models.Model):
    """ Clase que define todo lo referente a los Candidatos:
        Registrar, Modificar, Eliminar y Consultar

        :param CharField nombre: campo donde registra el nombre del candidato.
        :param CharField apellido: campo donde registra el apellido del candidato.
        :param CharField cedula: campo donde registra la cedula del candidato.
        :param ImageField foto: campo de tipo imagen para guardar la foto del candidato
        :param CharField sexo: campo donde seleccionamos el sexo el candidato.
        :param IntegerField edad: campo de tipo entero para la edad del candidato.
        :param CharField twitter: campo para ingresar el twitter del candidato
        :param CharField part_politico: campo de Seleccion del partido politico
        :param ForeignKey user_create: campo que llama al modelo User.
        :param ForeignKey user_update: campo que llama al modelo User.
        :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
        :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
        :param CharField categoria: campo donde registran las categorias.
    """

    nombre = models.CharField(verbose_name="Nombre del Candidato", max_length=100)
    apellido = models.CharField(verbose_name="Apellido del Candidato", max_length=100)
    cedula = models.CharField(max_length=8, verbose_name="Cédula", unique=True)
    foto = models.ImageField(upload_to=generate_new_filename)
    sexo = models.CharField(choices=SEXO, default=0, max_length=15)
    edad = models.IntegerField()
    twitter = models.CharField(max_length=200, null=True, blank=True)
    part_politico = models.ForeignKey(Partidos, verbose_name="Partido Político")
    candidato_activo = models.BooleanField(default=False)
    foto_binario = models.TextField(null=True, blank=True)

    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """
            :param unique_together: verifica que no existan candidatos repetidos en base a su cedula apellido y nombre
            :param ordering: Ordena los registros en base a el campo nombre y apellido
        """
        unique_together = ("cedula", "nombre", "apellido")
        ordering = ('nombre', 'apellido')

    def __unicode__(self):
        """
            :returns: Representacion en cadena de la clase Candidatos
        """
        return self.nombre

    def get_absolute_url(self):
        """
            :returns: La Url de vista principal de administracion de Candidatos
        """
        return ('listar_candidatos', [self.id, ])
