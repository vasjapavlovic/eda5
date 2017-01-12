# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0014_auto_20170111_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='najemlastnine',
            name='veljavnost_trajanje_opisno',
            field=models.CharField(null=True, blank=True, verbose_name='trajanje pogodbe - opisno', max_length=255),
        ),
    ]
