# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0004_auto_20151220_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skupinadokumenta',
            options={'verbose_name': 'Skupina Dokumentov', 'verbose_name_plural': 'Skupine Dokumentov', 'ordering': ('zap_st',)},
        ),
        migrations.AlterModelOptions(
            name='vrstadokumenta',
            options={'verbose_name': 'Vrsta Dokumenta', 'verbose_name_plural': 'Vrste Dokumentov', 'ordering': ('zap_st',)},
        ),
    ]
