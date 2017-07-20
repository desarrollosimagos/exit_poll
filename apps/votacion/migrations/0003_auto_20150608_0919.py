# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacion', '0002_votacion_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votacion',
            name='grupo_etareo',
            field=models.IntegerField(max_length=2),
            preserve_default=True,
        ),
    ]
