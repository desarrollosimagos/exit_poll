# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0001_initial'),
        ('estados', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExitPoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('municipio', models.IntegerField(null=True, blank=True)),
                ('parroquia', models.IntegerField(null=True, blank=True)),
                ('circuito', models.IntegerField(null=True, blank=True)),
                ('sector', models.IntegerField(null=True, blank=True)),
                ('poligonal', models.IntegerField(null=True, blank=True)),
                ('centro', models.IntegerField(null=True, blank=True)),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('candidatos', models.ForeignKey(to='candidatos.Candidatos', null=True)),
                ('eleccion', models.ForeignKey(to='elecciones.Eleccion', null=True)),
                ('estado', models.ForeignKey(related_name='estado_exitpoll', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', blank=True, to='estados.Estado', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('eleccion', 'candidatos', 'estado', 'municipio', 'circuito', 'sector', 'poligonal', 'centro'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='exitpoll',
            unique_together=set([('eleccion', 'candidatos')]),
        ),
    ]
