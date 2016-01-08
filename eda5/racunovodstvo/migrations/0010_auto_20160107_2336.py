# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0009_auto_20160106_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='datum_storitve_do',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='racun',
            name='datum_storitve_od',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='racun',
            name='valuta',
            field=models.DateField(null=True, blank=True),
        ),
    ]
