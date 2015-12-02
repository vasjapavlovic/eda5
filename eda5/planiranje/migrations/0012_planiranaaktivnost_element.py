# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0007_auto_20151201_1847'),
        ('planiranje', '0011_planiranaaktivnost_naziv_opravila_izven_plana'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranaaktivnost',
            name='element',
            field=models.ForeignKey(blank=True, null=True, to='deli.Element'),
        ),
    ]
