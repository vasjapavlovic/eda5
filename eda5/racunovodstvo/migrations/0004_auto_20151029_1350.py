# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0003_konto_skupinastroska_strosek_vrstastroska'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SkupinaStroska',
            new_name='SkupinaVrsteStroska',
        ),
        migrations.AlterModelOptions(
            name='konto',
            options={'verbose_name_plural': 'konti', 'verbose_name': 'konto'},
        ),
        migrations.AlterModelOptions(
            name='skupinavrstestroska',
            options={'verbose_name_plural': 'skupine vrst stroškov', 'verbose_name': 'skupina vrste stroška'},
        ),
        migrations.AlterModelOptions(
            name='vrstastroska',
            options={'verbose_name_plural': 'vrste stroškov', 'verbose_name': 'vrsta stroška'},
        ),
    ]
