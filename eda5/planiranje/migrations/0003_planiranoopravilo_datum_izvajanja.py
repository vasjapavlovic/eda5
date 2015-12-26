# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0002_auto_20151226_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranoopravilo',
            name='datum_izvajanja',
            field=models.DateField(blank=True, null=True),
        ),
    ]
