# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0004_arhiviranje_racun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arhiv',
            name='oznaka',
            field=models.CharField(verbose_name='oznaka', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='arhivmesto',
            name='oznaka',
            field=models.CharField(verbose_name='oznaka', max_length=50),
        ),
    ]
