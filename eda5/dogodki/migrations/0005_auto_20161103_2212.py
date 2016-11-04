# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0004_auto_20161101_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='is_potrebna_prijava_policiji',
            field=models.NullBooleanField(verbose_name='potrebna prijava policiji?'),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='povzrocitelj',
            field=models.CharField(blank=True, max_length=255, verbose_name='povzročitelj (opisno)'),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='predvidena_visina_skode',
            field=models.DecimalField(max_digits=7, blank=True, decimal_places=2, null=True, verbose_name='predvidena višina škode'),
        ),
    ]
