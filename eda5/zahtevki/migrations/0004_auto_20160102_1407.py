# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0003_auto_20151230_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zahtevek',
            name='vrsta',
            field=models.IntegerField(choices=[(1, 'Škodni Dogodek'), (2, 'Sestanek'), (3, 'Izvedba del'), (4, 'Predaja Lastnine')]),
        ),
    ]
