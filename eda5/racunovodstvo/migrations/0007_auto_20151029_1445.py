# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0006_auto_20151029_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='podkonto',
            options={'verbose_name_plural': 'pod konti', 'verbose_name': 'pod konto', 'ordering': ('zap_st',)},
        ),
        migrations.AddField(
            model_name='podkonto',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna Številka', default=0),
        ),
    ]
