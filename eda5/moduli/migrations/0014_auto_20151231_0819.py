# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0013_auto_20151231_0819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modul',
            options={'ordering': ['zap_st', 'naziv'], 'verbose_name': 'modul', 'verbose_name_plural': 'moduli'},
        ),
        migrations.AlterModelOptions(
            name='zavihek',
            options={'ordering': ['zap_st', 'oznaka'], 'verbose_name': 'zavihek', 'verbose_name_plural': 'zavihki'},
        ),
        migrations.AddField(
            model_name='modul',
            name='zap_st',
            field=models.IntegerField(default=9999, verbose_name='zaporedna številka'),
        ),
        migrations.AddField(
            model_name='zavihek',
            name='zap_st',
            field=models.IntegerField(default=9999, verbose_name='zaporedna številka'),
        ),
    ]
