# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.posta.models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0003_auto_20151026_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='priponka',
            field=models.FileField(blank=True, upload_to=eda5.posta.models.Dokument.dokument_directory_path),
        ),
    ]
