# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lokacija', '0002_auto_20170226_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etaza',
            name='naziv',
            field=models.CharField(blank=True, verbose_name='Naziv', null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='prostor',
            name='naziv',
            field=models.CharField(blank=True, verbose_name='Naziv', null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='stavba',
            name='naziv',
            field=models.CharField(blank=True, verbose_name='Naziv', null=True, max_length=255),
        ),
    ]
