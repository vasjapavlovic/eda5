# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0002_auto_20151220_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zahteveksestanek',
            name='sklicatelj',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev', blank=True, null=True),
        ),
    ]
