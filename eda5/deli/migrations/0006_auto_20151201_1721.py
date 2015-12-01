# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0005_element_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='tovarniska_st',
            field=models.CharField(verbose_name='Tovarniška Številka', blank=True, max_length=100),
        ),
    ]
