# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacion', '0003_auto_20150608_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='votacion',
            name='circuito',
            field=models.IntegerField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='votacion',
            name='estado',
            field=models.IntegerField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='votacion',
            name='municipio',
            field=models.IntegerField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
    ]
