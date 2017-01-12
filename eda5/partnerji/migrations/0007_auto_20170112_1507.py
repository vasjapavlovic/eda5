# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0006_remove_partner_skupina_partnerja'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='kontakt_email',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='kontakt_tel',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]
