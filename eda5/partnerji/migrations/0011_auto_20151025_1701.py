# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0010_auto_20151025_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='davcna_st',
            field=models.CharField(unique=True, blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='partner',
            name='dolgo_ime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='partner',
            name='maticna_st',
            field=models.CharField(unique=True, blank=True, max_length=15),
        ),
    ]
