# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0003_auto_20151203_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delovrsta',
            old_name='sklop',
            new_name='skupina',
        ),
        migrations.AlterField(
            model_name='delovrsta',
            name='oznaka',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='delovrstasklop',
            name='oznaka',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
