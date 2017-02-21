# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0010_auto_20170221_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomanjkljivost',
            name='opis_text',
            field=models.TextField(null=True, verbose_name='Problem', blank=True),
        ),
    ]
