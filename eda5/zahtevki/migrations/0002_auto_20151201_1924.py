# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zahtevek',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='zahtevek',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
