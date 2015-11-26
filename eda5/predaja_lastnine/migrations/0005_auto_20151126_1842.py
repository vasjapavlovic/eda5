# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predaja_lastnine', '0004_auto_20151126_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daljinec',
            options={'verbose_name_plural': 'daljinci', 'verbose_name': 'daljinec'},
        ),
        migrations.AddField(
            model_name='daljinec',
            name='oznaka',
            field=models.CharField(default='0001', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daljinec',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, 'v uporabi'), (2, 'izklopljen')]),
        ),
        migrations.AddField(
            model_name='daljinec',
            name='stevilka',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
