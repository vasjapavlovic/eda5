# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Strosek',
        ),
        migrations.AlterModelOptions(
            name='strosekle',
            options={'verbose_name': 'strošek na LE', 'verbose_name_plural': 'stroški na LE'},
        ),
    ]
