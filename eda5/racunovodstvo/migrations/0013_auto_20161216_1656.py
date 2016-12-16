# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0004_auto_20160105_1048'),
        ('racunovodstvo', '0012_auto_20160214_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='obdelan_racunovodstvo',
            field=models.NullBooleanField(verbose_name='obdelan iz strani računovodskega servisa', default=False),
        ),
        migrations.AddField(
            model_name='racun',
            name='povracilo_stroskov_zaposlenemu',
            field=models.ForeignKey(blank=True, to='partnerji.Oseba', null=True),
        ),
    ]
