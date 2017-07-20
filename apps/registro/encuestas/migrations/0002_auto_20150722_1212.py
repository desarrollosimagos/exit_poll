# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='url_web',
        ),
        migrations.AddField(
            model_name='encuesta',
            name='tipo_aplicacion',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='tipo',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'1', b'Web'), (b'2', b'M\xc3\xb3vil'), (b'3', b'Web y M\xc3\xb3vil')]),
            preserve_default=True,
        ),
    ]
