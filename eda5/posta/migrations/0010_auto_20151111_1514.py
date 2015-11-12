# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0009_auto_20151111_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='naslovnik',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='naslovnik', verbose_name='naslovnik'),
        ),
        migrations.AlterField(
            model_name='dokument',
            name='posiljatelj',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='posiljatelj', verbose_name='pošiljatelj'),
        ),
    ]
