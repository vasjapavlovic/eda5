# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nadzornaplosca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nadzornaenota',
            options={'ordering': ['oznaka'], 'verbose_name': 'nadzorna enota', 'verbose_name_plural': 'nadzorne enote'},
        ),
    ]
