# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0007_auto_20170112_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='kontakt_email',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='kontakt_tel',
            field=models.CharField(null=True, max_length=15, blank=True),
        ),
    ]
