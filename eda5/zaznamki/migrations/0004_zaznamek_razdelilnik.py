# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0005_razdelilnik_zahtevek'),
        ('zaznamki', '0003_zaznamek_povprasevanje'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaznamek',
            name='razdelilnik',
            field=models.ForeignKey(to='razdelilnik.Razdelilnik', null=True, blank=True),
        ),
    ]
