# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0010_auto_20151211_2100'),
        ('narocila', '0002_auto_20151203_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='narocilotelefon',
            name='oseba',
            field=models.ForeignKey(to='partnerji.Oseba', null=True, blank=True),
        ),
    ]
