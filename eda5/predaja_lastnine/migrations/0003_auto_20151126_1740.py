# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predaja_lastnine', '0002_daljinec_predajadaljinca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predajalastnine',
            name='dokument',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='predajalastnine',
            name='trajanje',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
