# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0013_auto_20170219_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opravilo',
            name='element',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', blank=True),
        ),
    ]
