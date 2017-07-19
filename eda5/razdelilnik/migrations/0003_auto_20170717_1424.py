# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0002_razdelilnik_razdelilnikracun'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='razdelilnik',
            options={'verbose_name': 'Razdelilnik', 'verbose_name_plural': 'Razdelilniki', 'ordering': ('-obdobje_obracuna_leto', '-obdobje_obracuna_mesec')},
        ),
    ]
