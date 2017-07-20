# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partidos',
            name='partido_binario',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
