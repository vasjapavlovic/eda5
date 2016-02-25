# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obvestila', '0006_povezava'),
    ]

    operations = [
        migrations.AddField(
            model_name='povezava',
            name='url_detail',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='povezava',
            name='predtext',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='povezava',
            name='url_ref',
            field=models.CharField(max_length=500),
        ),
    ]
