# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0020_auto_20160214_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='avtor',
            field=models.ForeignKey(related_name='avtor', to='partnerji.SkupinaPartnerjev'),
        ),
    ]
