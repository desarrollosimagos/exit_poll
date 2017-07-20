# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sectores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='sector',
            field=models.CharField(max_length=150, verbose_name=b'Sector'),
            preserve_default=True,
        ),
    ]
