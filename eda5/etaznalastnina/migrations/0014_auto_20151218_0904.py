# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0013_auto_20151218_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internadodatno',
            name='lastnik',
            field=models.ForeignKey(blank=True, to='partnerji.SkupinaPartnerjev', null=True, related_name='lastnik'),
        ),
    ]
