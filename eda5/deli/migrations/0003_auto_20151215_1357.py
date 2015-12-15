# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0002_auto_20151203_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podskupina',
            name='oznaka',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='skupina',
            name='oznaka',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
