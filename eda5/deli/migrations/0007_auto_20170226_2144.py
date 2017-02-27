# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0006_auto_20170226_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projektnomesto',
            name='bim_id',
            field=models.CharField(max_length=100, blank=True, null=True, verbose_name='BIM ID'),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='del_stavbe',
            field=models.ForeignKey(verbose_name='Del Stavbe', to='deli.DelStavbe'),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='funkcija',
            field=models.CharField(max_length=255, blank=True, null=True, verbose_name='Funkcija Elementa'),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='naziv',
            field=models.CharField(max_length=255, verbose_name='Naziv'),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='oznaka',
            field=models.CharField(verbose_name='Oznaka', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='tip_elementa',
            field=models.ForeignKey(verbose_name='Tip Elementa', to='katalog.TipArtikla'),
        ),
    ]
