# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0012_strosekrazdelilnikpostavka_delilnik_vrednost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racunrazdelilnik',
            name='racun',
        ),
        migrations.RemoveField(
            model_name='racunrazdelilnik',
            name='razdelilnik',
        ),
        migrations.DeleteModel(
            name='RacunRazdelilnik',
        ),
    ]
