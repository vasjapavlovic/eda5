# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0003_auto_20151029_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lastniskaenotaelaborat',
            options={'ordering': ('oznaka',), 'verbose_name': 'lastniška enota elaborat', 'verbose_name_plural': 'lastniške enote elaborat'},
        ),
        migrations.AlterModelOptions(
            name='lastniskaenotainterna',
            options={'ordering': ('oznaka',), 'verbose_name': 'lastniška enota interna', 'verbose_name_plural': 'lastniške enote interna'},
        ),
    ]
