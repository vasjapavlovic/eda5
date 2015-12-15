# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0007_konto_zap_st'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='konto',
            options={'verbose_name': 'konto', 'ordering': ('zap_st',), 'verbose_name_plural': 'konti'},
        ),
        migrations.AlterField(
            model_name='konto',
            name='oznaka',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='podkonto',
            name='oznaka',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='skupinavrstestroska',
            name='oznaka',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='vrstastroska',
            name='skupina',
            field=models.ForeignKey(to='racunovodstvo.SkupinaVrsteStroska', unique=True),
        ),
    ]
