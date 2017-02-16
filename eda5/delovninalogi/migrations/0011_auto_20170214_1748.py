# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0010_auto_20170214_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delo',
            name='opis',
        ),
        migrations.AddField(
            model_name='delo',
            name='naziv',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delo',
            name='oznaka',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
