# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0014_auto_20170330_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='naloga',
            name='pomanjkljivost',
            field=models.ForeignKey(null=True, verbose_name='Povezava na pomanjkljivost', blank=True, to='pomanjkljivosti.Pomanjkljivost'),
        ),
        migrations.AlterField(
            model_name='naloga',
            name='zahtevek',
            field=models.ForeignKey(null=True, verbose_name='Rešuje se pod Zahtevkom', blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
