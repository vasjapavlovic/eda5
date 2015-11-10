# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0009_auto_20151110_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delovninalog',
            name='datum_plan',
            field=models.DateField(null=True, verbose_name='V planu za dne', blank=True),
        ),
    ]
