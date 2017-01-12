# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0008_auto_20170112_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='kontakt_tel',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
