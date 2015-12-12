# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0005_auto_20151206_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='maticna_st',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]
