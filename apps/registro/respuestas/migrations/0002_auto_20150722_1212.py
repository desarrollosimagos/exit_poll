# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respuestas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestas',
            name='respuesta',
            field=models.CharField(max_length=200, verbose_name=b'Descripcion de la Respuestas'),
            preserve_default=True,
        ),
    ]
