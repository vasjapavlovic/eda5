# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.deli.models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0006_auto_20151030_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='dokumentacija',
            field=models.FileField(blank=True, verbose_name='dokumentacija', upload_to=eda5.deli.models.Element.dokumentacija_directory_path),
        ),
    ]
