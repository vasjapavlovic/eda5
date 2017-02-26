# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0006_planiranoopravilo_zmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranoopravilo',
            name='datum_naslednjega_opravila',
            field=models.DateField(blank=True, null=True),
        ),
    ]
