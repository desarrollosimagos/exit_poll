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
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_s', models.IntegerField(max_length=2, verbose_name=b'C\xc3\xb3digo del Sector')),
                ('sector', models.CharField(max_length=150, verbose_name=b'Nombre del Centro Electoral')),
                ('municipio', models.IntegerField(null=True)),
                ('parroquia', models.IntegerField(null=True)),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.ForeignKey(related_name='estado_sectores', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', to='estados.Estado', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('cod_s', 'sector', 'estado', 'municipio', 'parroquia'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sector',
            unique_together=set([('cod_s', 'sector', 'estado', 'municipio', 'parroquia')]),
        ),
    ]
