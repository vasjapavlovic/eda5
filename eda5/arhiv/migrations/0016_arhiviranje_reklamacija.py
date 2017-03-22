# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reklamacije', '0001_initial'),
        ('arhiv', '0015_auto_20170209_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='reklamacija',
            field=models.ForeignKey(null=True, blank=True, to='reklamacije.Reklamacija'),
        ),
    ]
