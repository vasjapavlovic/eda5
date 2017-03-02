# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0010_partner_partner_skupina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='kratko_ime',
            field=models.CharField(verbose_name='Kratko Ime', max_length=100),
        ),
        migrations.AlterField(
            model_name='partner',
            name='naslov',
            field=models.CharField(verbose_name='Naslov', max_length=255),
        ),
    ]
