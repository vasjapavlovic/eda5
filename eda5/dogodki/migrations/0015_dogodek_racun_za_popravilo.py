# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0015_auto_20170209_1601'),
        ('dogodki', '0014_auto_20170214_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='racun_za_popravilo',
            field=models.ForeignKey(to='arhiv.Arhiviranje', null=True, blank=True, related_name='racun_za_popravilo'),
        ),
    ]
