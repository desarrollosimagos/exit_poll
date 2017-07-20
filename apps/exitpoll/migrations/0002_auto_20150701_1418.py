# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exitpoll', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exitpoll',
            options={'ordering': ('eleccion', 'candidatos', 'estado', 'municipio', 'circuito', 'sector', 'poligonal')},
        ),
        migrations.RemoveField(
            model_name='exitpoll',
            name='centro',
        ),
    ]
