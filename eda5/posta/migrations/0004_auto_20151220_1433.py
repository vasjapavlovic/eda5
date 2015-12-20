# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0003_auto_20151220_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skupinadokumenta',
            name='oznaka',
            field=models.CharField(max_length=3, verbose_name='oznaka', unique=True),
        ),
        migrations.AlterField(
            model_name='vrstadokumenta',
            name='oznaka',
            field=models.CharField(max_length=3, verbose_name='oznaka', unique=True),
        ),
    ]
