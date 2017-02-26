# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0007_planiranoopravilo_datum_naslednjega_opravila'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranoopravilo',
            name='datum_izvedeno_dne',
            field=models.DateField(null=True, verbose_name='Izvedeno dne', blank=True),
        ),
        migrations.AlterField(
            model_name='planiranoopravilo',
            name='datum_naslednjega_opravila',
            field=models.DateField(null=True, verbose_name='Naslednji pregled', blank=True),
        ),
    ]
