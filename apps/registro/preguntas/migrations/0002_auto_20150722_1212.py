# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='pregunta',
            field=models.CharField(max_length=300, verbose_name=b'Descripcion de la Pregunta'),
            preserve_default=True,
        ),
    ]
