# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zahtevek',
            options={'verbose_name': 'zahtevek', 'verbose_name_plural': 'zahtevki', 'ordering': ('-oznaka',)},
        ),
        migrations.AlterModelOptions(
            name='zahtevekizvedbadela',
            options={'verbose_name': 'izvedba dela', 'verbose_name_plural': 'izvedba del', 'ordering': ('-zahtevek__oznaka',)},
        ),
        migrations.AlterModelOptions(
            name='zahteveksestanek',
            options={'verbose_name': 'sestanek', 'verbose_name_plural': 'sestanki', 'ordering': ('-zahtevek__oznaka',)},
        ),
    ]
