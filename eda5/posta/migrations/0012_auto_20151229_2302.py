# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0011_dokument_oznaka_baza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='avtor',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='pošiljatelj'),
        ),
    ]
