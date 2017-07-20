# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EncuestaResultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_respuesta', models.IntegerField(verbose_name=b'C\xc3\xb3digo Respuesta')),
                ('otras', models.CharField(max_length=150, null=True, verbose_name=b'Otras', blank=True)),
                ('cod_encuesta', models.IntegerField(null=True, verbose_name=b'C\xc3\xb3digo Encuesta', blank=True)),
                ('num_encuestado', models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero de Encuestados', blank=True)),
                ('grupo_etareo', models.IntegerField(max_length=2, null=True, blank=True)),
                ('sexo', models.CharField(default=0, max_length=15, null=True, blank=True, choices=[(b'1', b'Femenino'), (b'2', b'Masculino')])),
                ('estado', models.IntegerField(max_length=3, null=True, blank=True)),
                ('municipio', models.IntegerField(max_length=3, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
