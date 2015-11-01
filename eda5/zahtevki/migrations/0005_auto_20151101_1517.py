# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0013_auto_20151030_1310'),
        ('zahtevki', '0004_auto_20151101_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='zahteveksestanek',
            name='udelezenci',
            field=models.ManyToManyField(to='partnerji.Oseba', verbose_name='udeleženci'),
        ),
        migrations.AlterField(
            model_name='zahtevekskodnidogodek',
            name='predvidena_visina_skode',
            field=models.DecimalField(max_digits=7, null=True, decimal_places=2, verbose_name='predvidena višina škode', blank=True),
        ),
    ]
