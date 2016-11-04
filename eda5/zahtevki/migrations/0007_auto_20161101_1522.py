# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0006_auto_20161031_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zahtevek',
            name='status',
            field=models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'preklicano')], default=0),
        ),
    ]
