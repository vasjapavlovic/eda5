# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0011_modul_zap_st'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modul',
            options={'ordering': ['zap_st', 'naziv'], 'verbose_name_plural': 'moduli', 'verbose_name': 'modul'},
        ),
        migrations.AlterModelOptions(
            name='zavihek',
            options={'ordering': ['zap_st', 'oznaka'], 'verbose_name_plural': 'zavihki', 'verbose_name': 'zavihek'},
        ),
        migrations.AddField(
            model_name='zavihek',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=0),
        ),
    ]
