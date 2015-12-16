# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0003_modul_url_ref'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modul',
            options={'verbose_name_plural': 'moduli', 'ordering': ['naziv'], 'verbose_name': 'modul'},
        ),
    ]
