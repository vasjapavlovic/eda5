# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0007_auto_20160102_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='najemlastnine',
            name='lastniska_enota',
            field=models.ForeignKey(verbose_name='LE', to='etaznalastnina.LastniskaEnotaInterna', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='najemlastnine',
            name='placnik',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev'),
        ),
    ]
