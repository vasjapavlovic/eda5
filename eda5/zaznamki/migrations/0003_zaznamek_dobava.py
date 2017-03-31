# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skladisce', '0001_initial'),
        ('zaznamki', '0002_zaznamek_reklamacija'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaznamek',
            name='dobava',
            field=models.ForeignKey(null=True, to='skladisce.Dobava', blank=True),
        ),
    ]
