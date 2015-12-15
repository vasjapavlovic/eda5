# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0010_auto_20151211_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posta',
            options={'verbose_name_plural': 'Pošte', 'verbose_name': 'Pošta', 'ordering': ['postna_stevilka']},
        ),
    ]
