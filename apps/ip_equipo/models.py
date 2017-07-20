from django.db import models


class IpEquipo(models.Model):
    """ Clase donde se guarda la ip del equipo y el pk de la encuesta:


    :param IntegerField cod_encuesta: campo donde se coloca el codigo de la Encuesta.
    :param CharField estado: campo donde ingresas la ip del equipo que envio la encuesta.
    """

    cod_encuesta = models.IntegerField()
    ip_equipo = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ip_equipo

    def get_absolute_url(self):

        return ('listar_equipos', [self.id, ])
