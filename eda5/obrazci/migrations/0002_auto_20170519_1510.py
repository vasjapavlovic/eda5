# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obrazci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obrazecsplosno',
            name='priloge',
            field=models.ManyToManyField(blank=True, to='arhiv.Arhiviranje', verbose_name='Priloge'),
        ),
    ]
