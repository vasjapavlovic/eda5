# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0012_auto_20160102_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predajalastnine',
            name='zahtevek',
            field=models.OneToOneField(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
