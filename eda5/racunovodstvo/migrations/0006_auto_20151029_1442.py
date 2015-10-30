# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0005_auto_20151029_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='konto',
            options={'verbose_name_plural': 'konti', 'ordering': ('oznaka',), 'verbose_name': 'konto'},
        ),
        migrations.AlterModelOptions(
            name='podkonto',
            options={'verbose_name_plural': 'pod konti', 'ordering': ('oznaka',), 'verbose_name': 'pod konto'},
        ),
        migrations.AlterModelOptions(
            name='skupinavrstestroska',
            options={'verbose_name_plural': 'skupine vrst stroškov', 'ordering': ('zap_st',), 'verbose_name': 'skupina vrste stroška'},
        ),
        migrations.AlterModelOptions(
            name='strosek',
            options={'verbose_name_plural': 'stroški', 'ordering': ('oznaka',), 'verbose_name': 'strošek'},
        ),
        migrations.AlterModelOptions(
            name='vrstastroska',
            options={'verbose_name_plural': 'vrste stroškov', 'ordering': ('zap_st',), 'verbose_name': 'vrsta stroška'},
        ),
    ]
