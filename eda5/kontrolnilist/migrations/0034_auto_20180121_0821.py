# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0033_auto_20180121_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontrolavrednost',
            name='vrednost_yes_no',
            field=models.IntegerField(blank=True, choices=[(0, 'DA'), (1, 'NE')], null=True, verbose_name='vrednost DA/NE'),
        ),
        migrations.AlterField(
            model_name='kontrolaspecifikacija',
            name='vrednost_vrsta',
            field=models.IntegerField(default=1, verbose_name='vrsta vrednosti', choices=[(1, 'check'), (2, 'text'), (4, 'number'), (5, 'yes_no'), (3, 'select')]),
        ),
    ]
