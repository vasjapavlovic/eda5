# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0002_auto_20151215_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='modul',
            name='url_ref',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
