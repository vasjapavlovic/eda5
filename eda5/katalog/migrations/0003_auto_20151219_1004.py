# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0002_auto_20151219_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelartikla',
            old_name='tip',
            new_name='tip_artikla',
        ),
        migrations.AddField(
            model_name='proizvajalec',
            name='oznaka',
            field=models.CharField(default='novo', unique=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proizvajalec',
            name='naziv',
            field=models.CharField(max_length=100),
        ),
    ]
