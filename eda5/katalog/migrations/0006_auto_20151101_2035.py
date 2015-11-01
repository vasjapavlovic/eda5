# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0005_auto_20151030_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planov',
            name='perioda_predpisana_enota',
            field=models.CharField(verbose_name='enota periode', max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')]),
        ),
    ]
