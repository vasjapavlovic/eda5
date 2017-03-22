# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reklamacije', '0001_initial'),
        ('zaznamki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaznamek',
            name='reklamacija',
            field=models.ForeignKey(blank=True, null=True, to='reklamacije.Reklamacija'),
        ),
    ]
