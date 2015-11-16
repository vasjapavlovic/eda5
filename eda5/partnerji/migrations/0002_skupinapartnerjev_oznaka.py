# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skupinapartnerjev',
            name='oznaka',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
