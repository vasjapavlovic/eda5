# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_remove_projektnomesto_tip_elementa'),
    ]

    operations = [
        migrations.AddField(
            model_name='delstavbe',
            name='stavba',
            field=models.ForeignKey(null=True, to='deli.Stavba', blank=True),
        ),
    ]
