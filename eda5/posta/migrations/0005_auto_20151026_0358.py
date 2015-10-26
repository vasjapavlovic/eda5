# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0004_auto_20151026_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='priponka',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
