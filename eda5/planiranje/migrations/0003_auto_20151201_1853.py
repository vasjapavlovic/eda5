# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0002_remove_planizdaja_potrditvena_dokumentacija'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planopravilo',
            name='zap_st',
        ),
        migrations.AlterField(
            model_name='planopravilo',
            name='opomba',
            field=models.TextField(blank=True),
        ),
    ]
