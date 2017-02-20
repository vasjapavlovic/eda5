# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0011_auto_20170214_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vzorecopravila',
            name='element',
            field=models.ManyToManyField(to='deli.ProjektnoMesto'),
        ),
    ]
