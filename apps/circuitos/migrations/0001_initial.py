# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n_circuito', models.CharField(max_length=2, verbose_name=b'Numero del circuito')),
                ('num_max_candidatos', models.IntegerField(verbose_name=b'Numero maximo de candidatos')),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.ForeignKey(related_name='estado_circuito', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', to='estados.Estado', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('estado', 'n_circuito'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='circuito',
            unique_together=set([('n_circuito', 'estado')]),
        ),
    ]
