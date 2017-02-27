# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0012_auto_20170227_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etaza',
            name='elevation',
            field=models.IntegerField(blank=True, null=True, verbose_name='Višinska kota Etaže'),
        ),
    ]
