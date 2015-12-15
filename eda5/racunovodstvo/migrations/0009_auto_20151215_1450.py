# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0008_auto_20151215_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrstastroska',
            name='oznaka',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='vrstastroska',
            name='skupina',
            field=models.ForeignKey(to='racunovodstvo.SkupinaVrsteStroska'),
        ),
    ]
