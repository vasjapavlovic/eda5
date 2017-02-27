# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0013_auto_20170227_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etaza',
            name='elevation',
            field=models.DecimalField(blank=True, null=True, verbose_name='Višinska kota Etaže', decimal_places=5, max_digits=20),
        ),
    ]
