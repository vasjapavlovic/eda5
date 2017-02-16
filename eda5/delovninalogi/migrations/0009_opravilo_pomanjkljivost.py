# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0007_auto_20170214_1412'),
        ('delovninalogi', '0008_auto_20170209_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='pomanjkljivost',
            field=models.ManyToManyField(to='pomanjkljivosti.Pomanjkljivost', blank=True),
        ),
    ]
