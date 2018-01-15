# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0015_auto_20180111_1444'),
        ('delovninalogi', '0013_auto_20180114_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='vzorecopravila',
            name='aktivnost',
            field=models.ManyToManyField(to='kontrolnilist.Aktivnost', blank=True),
        ),
        migrations.AlterField(
            model_name='vzorecopravila',
            name='element',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', blank=True),
        ),
        migrations.AlterField(
            model_name='vzorecopravila',
            name='vrsta_stroska',
            field=models.ForeignKey(null=True, verbose_name='stroškovno mesto', to='racunovodstvo.VrstaStroska', blank=True),
        ),
    ]
