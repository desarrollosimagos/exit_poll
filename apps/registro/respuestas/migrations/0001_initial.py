# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_respuesta', models.IntegerField(max_length=4, verbose_name=b'C\xc3\xb3digo de Respuestas')),
                ('respuesta', models.CharField(max_length=150, verbose_name=b'Descripcion de la Respuestas')),
                ('tipo', models.CharField(default=1, max_length=2, choices=[(b'1', b'Cerrada'), (b'2', b'Abierta')])),
                ('fecha_create', models.DateField(auto_now_add=True)),
                ('fecha_update', models.DateField(auto_now=True, null=True)),
                ('cod_pregunta', models.ForeignKey(to='preguntas.Preguntas')),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='respuestas',
            unique_together=set([('cod_pregunta', 'cod_respuesta', 'respuesta')]),
        ),
    ]
