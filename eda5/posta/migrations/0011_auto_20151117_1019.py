# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.posta.models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0010_auto_20151117_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='priponka',
            field=models.FileField(null=True, blank=True, upload_to=eda5.posta.models.Dokument.dokument_directory_path),
        ),
    ]
