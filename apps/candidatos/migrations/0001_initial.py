# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import apps.candidatos.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre del Candidato')),
                ('apellido', models.CharField(max_length=100, verbose_name=b'Apellido del Candidato')),
                ('cedula', models.CharField(unique=True, max_length=8, verbose_name=b'C\xc3\xa9dula')),
                ('foto', models.ImageField(upload_to=apps.candidatos.models.generate_new_filename)),
                ('sexo', models.CharField(default=0, max_length=15, choices=[(b'1', b'Femenino'), (b'2', b'Masculino')])),
                ('edad', models.IntegerField()),
                ('twitter', models.CharField(max_length=200, null=True, blank=True)),
                ('candidato_activo', models.BooleanField(default=False)),
                ('fecha_create', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('part_politico', models.ForeignKey(verbose_name=b'Partido Pol\xc3\xadtico', to='partidos.Partidos')),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('nombre', 'apellido'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='candidatos',
            unique_together=set([('cedula', 'nombre', 'apellido')]),
        ),
    ]
