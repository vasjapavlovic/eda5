# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predaja_lastnine', '0005_auto_20151126_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='predajadaljinca',
            options={'verbose_name': 'predaja daljinca', 'verbose_name_plural': 'predaje daljincev'},
        ),
        migrations.AddField(
            model_name='predajadaljinca',
            name='daljinec',
            field=models.ForeignKey(default=1, to='predaja_lastnine.Daljinec'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predajadaljinca',
            name='datum',
            field=models.DateField(default='2015-11-26'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predajadaljinca',
            name='oznaka',
            field=models.CharField(max_length=4, default='0001'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predajadaljinca',
            name='predaja_lastnine',
            field=models.ForeignKey(default=1, to='predaja_lastnine.PredajaLastnine'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predajalastnine',
            name='daljinec',
            field=models.ManyToManyField(through='predaja_lastnine.PredajaDaljinca', to='predaja_lastnine.Daljinec'),
        ),
        migrations.AlterField(
            model_name='predajalastnine',
            name='oznaka',
            field=models.CharField(max_length=4),
        ),
    ]
