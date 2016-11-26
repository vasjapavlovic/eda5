# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kljuci', '0006_predajakljuca_kolicina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predajakljuca',
            name='kolicina',
        ),
        migrations.AddField(
            model_name='predajakljuca',
            name='vrsta_predaje',
            field=models.IntegerField(default=1, choices=[(1, 'predaja'), (2, 'vračilo')]),
            preserve_default=False,
        ),
    ]
