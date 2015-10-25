# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banka',
            options={'verbose_name_plural': 'Banke', 'verbose_name': 'Banka'},
        ),
        migrations.AlterModelOptions(
            name='oseba',
            options={'verbose_name_plural': 'Osebe', 'verbose_name': 'Oseba'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name_plural': 'Partnerji', 'verbose_name': 'Partner'},
        ),
        migrations.AlterModelOptions(
            name='posta',
            options={'verbose_name_plural': 'Pošte', 'verbose_name': 'Pošta'},
        ),
        migrations.AlterModelOptions(
            name='trracun',
            options={'verbose_name_plural': 'TR Računi', 'verbose_name': 'TR Račun'},
        ),
    ]
