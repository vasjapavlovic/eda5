# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0007_auto_20161101_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opravilo',
            name='element',
            field=models.ManyToManyField(to='deli.ProjektnoMesto'),
        ),
    ]
