# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0005_auto_20170207_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='projektnomesto',
            name='bim_id',
            field=models.CharField(max_length=100, verbose_name='Tip Artikla', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='projektno_mesto',
            field=models.ForeignKey(to='deli.ProjektnoMesto', verbose_name='projektno mesto'),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='del_stavbe',
            field=models.ForeignKey(to='deli.DelStavbe', verbose_name='Tip Artikla'),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='naziv',
            field=models.CharField(max_length=255, verbose_name='oznaka'),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='oznaka',
            field=models.CharField(max_length=20, verbose_name='oznaka', unique=True),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='tip_elementa',
            field=models.ForeignKey(to='katalog.TipArtikla', verbose_name='Tip Artikla'),
        ),
    ]
