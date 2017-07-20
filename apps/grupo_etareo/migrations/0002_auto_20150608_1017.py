# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupo_etareo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo_etareo',
            options={'ordering': ('descripcion',)},
        ),
        migrations.RemoveField(
            model_name='grupo_etareo',
            name='grupo_etareo',
        ),
        migrations.AddField(
            model_name='grupo_etareo',
            name='desde',
            field=models.CharField(max_length=2, null=True, verbose_name=b'Desde', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grupo_etareo',
            name='hasta',
            field=models.CharField(max_length=2, null=True, verbose_name=b'Hasta', blank=True),
            preserve_default=True,
        ),
    ]
