# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0007_auto_20170214_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='prijava_dne',
            field=models.DateField(verbose_name='datum ugotovitve'),
        ),
    ]
