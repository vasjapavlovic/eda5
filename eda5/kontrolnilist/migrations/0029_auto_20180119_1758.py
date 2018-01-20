# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0028_auto_20180119_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktivnost',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=9999),
        ),
        migrations.AddField(
            model_name='kontrolaskupina',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=9999),
        ),
        migrations.AddField(
            model_name='kontrolaspecifikacija',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=9999),
        ),
        migrations.AddField(
            model_name='kontrolaspecifikacijaopcijaselect',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=9999),
        ),
    ]
