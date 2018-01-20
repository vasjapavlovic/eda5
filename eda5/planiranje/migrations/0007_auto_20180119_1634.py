# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0006_auto_20180119_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='plankontrolaskupina',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=9999),
        ),
        migrations.AddField(
            model_name='plankontrolaspecifikacija',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=9999),
        ),
        migrations.AddField(
            model_name='plankontrolaspecifikacijaopcijaselect',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=9999),
        ),
    ]
