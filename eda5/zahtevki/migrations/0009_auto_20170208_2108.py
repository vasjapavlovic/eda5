# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0008_auto_20161101_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zahtevek',
            name='narocilo',
        ),
        migrations.AlterField(
            model_name='zahteveksestanek',
            name='sklicatelj',
            field=models.ForeignKey(blank=True, to='partnerji.Partner', null=True),
        ),
    ]
