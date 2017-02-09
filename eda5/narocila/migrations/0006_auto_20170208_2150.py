# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0005_narocilo_zahtevek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narocilo',
            name='vrednost',
            field=models.DecimalField(null=True, max_digits=7, blank=True, decimal_places=2),
        ),
    ]
