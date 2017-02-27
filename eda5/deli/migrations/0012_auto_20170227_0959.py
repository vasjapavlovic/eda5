# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0011_auto_20170227_0703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lokacija',
            options={'verbose_name': 'Lokacija', 'ordering': ['prostor__oznaka'], 'verbose_name_plural': 'Lokacije'},
        ),
        migrations.AddField(
            model_name='etaza',
            name='elevation',
            field=models.DecimalField(null=True, verbose_name='Višinska kota Etaže', blank=True, decimal_places=2, max_digits=12),
        ),
    ]
