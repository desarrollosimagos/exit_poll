# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacion', '0004_auto_20150610_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='votacion',
            name='parroquia',
            field=models.IntegerField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='votacion',
            name='poligonal',
            field=models.IntegerField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='votacion',
            name='sector',
            field=models.IntegerField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
    ]
