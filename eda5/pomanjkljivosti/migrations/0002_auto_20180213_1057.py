# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0001_initial'),
        ('delovninalogi', '0002_auto_20180126_2341'),
        ('pomanjkljivosti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomanjkljivost',
            name='delovninalog',
            field=models.ManyToManyField(verbose_name='delovni nalog', blank=True, to='delovninalogi.DelovniNalog'),
        ),
        migrations.AddField(
            model_name='pomanjkljivost',
            name='dogodek',
            field=models.ManyToManyField(verbose_name='dogodek', blank=True, to='dogodki.Dogodek'),
        ),
    ]
