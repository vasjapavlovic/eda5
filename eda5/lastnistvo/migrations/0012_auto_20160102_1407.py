# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0004_auto_20160102_1407'),
        ('lastnistvo', '0011_najemlastnine_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='predajalastnine',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predajalastnine',
            name='oznaka',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
