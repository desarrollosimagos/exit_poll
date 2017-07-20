from django.db import models
from apps.topologia.estados.models import Estado
from django.contrib.auth.models import User


class Circuito(models.Model):
    """ Clase que define todo lo referente a los `Circuito`:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField n_circuito: campo donde registra el nombre del Circuito.
    :param ForeignKey estado: campo que llama al modelo Estado.
    :param IntegerField num_max_candidatos: campo de tipo entero para la cantidad maxima de candidatos por circuito
    :param ForeignKey user_create: campo que llama al modelo User.
    :param ForeignKey user_update: campo que llama al modelo User.
    :param DateTimeField fecha_create: campo de tipo tiempo que captura fecha y hora.
    :param DateTimeField fecha_update: campo de tipo tiempo que captura fecha y hora.
    """
    estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL,
                               related_name='estado_circuito', null=True)
    n_circuito = models.CharField(max_length=2, verbose_name="Numero del circuito",)
    num_max_candidatos = models.IntegerField(verbose_name="Numero maximo de candidatos")
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __unicode__(self):
        """
            :returns: Representacion en cadena de la clase Circuito
        """
        return self.n_circuito

    class Meta:
        """
            :param unique_together: verifica que no se registren circuitos con el mismo n_circuito y estado
            :param ordering: Ordena los registros en base a el campo estado y n_circuito
        """
        unique_together = ("n_circuito", "estado")
        ordering = ('estado', 'n_circuito')

    def get_absolute_url(self):
        """
            :returns: La Url de vista principal de administracion de Circuito
        """
        return ('listar_circuito', [self.id, ])
