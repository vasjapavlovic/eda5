# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predpis',
            name='oznaka',
            field=models.CharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='predpisopravilo',
            name='oznaka',
            field=models.CharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='predpispodsklop',
            name='oznaka',
            field=models.CharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='predpissklop',
            name='oznaka',
            field=models.CharField(unique=True, max_length=25),
        ),
    ]
