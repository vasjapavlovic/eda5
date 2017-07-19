# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('povprasevanje', '__first__'),
        ('zaznamki', '0002_remove_zaznamek_povprasevanje'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaznamek',
            name='povprasevanje',
            field=models.ForeignKey(null=True, to='povprasevanje.Povprasevanje', blank=True),
        ),
    ]
