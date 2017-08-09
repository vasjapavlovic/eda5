# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0006_racun_stavba'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='strosek',
            options={'ordering': ('-racun__racunovodsko_leto', '-racun__oznaka', '-oznaka'), 'verbose_name': 'strošek', 'verbose_name_plural': 'stroški'},
        ),
    ]
