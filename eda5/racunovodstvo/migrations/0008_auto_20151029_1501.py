# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0007_auto_20151029_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skupinavrstestroska',
            name='oznaka',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='strosek',
            name='oznaka',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vrstastroska',
            name='oznaka',
            field=models.CharField(max_length=20),
        ),
    ]
