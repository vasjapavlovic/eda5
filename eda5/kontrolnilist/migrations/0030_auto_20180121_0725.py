# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0029_auto_20180119_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontrolavrednost',
            name='vrednost_number',
            field=models.DecimalField(max_digits=50, null=True, max_length=255, verbose_name='vrednost število', blank=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='kontrolaspecifikacija',
            name='vrednost_vrsta',
            field=models.IntegerField(default=1, choices=[(1, 'check'), (2, 'text'), (2, 'number'), (3, 'select')], verbose_name='vrsta vrednosti'),
        ),
    ]
