# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.deli.models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0004_auto_20151030_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delstavbe',
            name='shema',
            field=models.FileField(blank=True, upload_to=eda5.deli.models.DelStavbe.shema_directory_path, verbose_name='shema sistema'),
        ),
    ]
