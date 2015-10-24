# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0003_auto_20151024_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modul',
            name='url_name',
            field=models.CharField(max_length=500),
        ),
    ]
