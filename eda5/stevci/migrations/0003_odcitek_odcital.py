# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0013_auto_20151030_1310'),
        ('stevci', '0002_auto_20151102_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='odcitek',
            name='odcital',
            field=models.ForeignKey(to='partnerji.Oseba', null=True, verbose_name='odčital', blank=True),
        ),
    ]
