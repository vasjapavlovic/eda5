# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0008_auto_20160102_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodajalastnine',
            name='placnik',
            field=models.ForeignKey(to='partnerji.SkupinaPartnerjev'),
        ),
    ]
