# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_auto_20151127_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='naziv',
        ),
        migrations.RemoveField(
            model_name='element',
            name='oznaka',
        ),
        migrations.AlterField(
            model_name='element',
            name='tovarniska_st',
            field=models.CharField(verbose_name='Tovarniška Številka', max_length=100),
        ),
    ]
