# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0003_lastniskaenotainterna_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastniskaenotaelaborat',
            name='povrsina_tlorisna_neto',
        ),
        migrations.RemoveField(
            model_name='lastniskaenotainterna',
            name='povrsina_tlorisna_neto',
        ),
    ]
