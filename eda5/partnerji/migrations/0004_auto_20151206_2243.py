# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0003_auto_20151206_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skupinapartnerjev',
            name='partner',
        ),
        migrations.AddField(
            model_name='partner',
            name='skupina_partnerjev',
            field=models.ManyToManyField(to='partnerji.SkupinaPartnerjev'),
        ),
    ]
