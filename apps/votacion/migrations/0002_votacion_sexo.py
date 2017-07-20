# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votacion',
            name='sexo',
            field=models.CharField(default=0, max_length=15, choices=[(b'1', b'Femenino'), (b'2', b'Masculino')]),
            preserve_default=True,
        ),
    ]
