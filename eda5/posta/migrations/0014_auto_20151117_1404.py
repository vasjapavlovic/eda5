# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0007_auto_20151117_1404'),
        ('delovninalogi', '0003_remove_delovninalog_dokument'),
        ('posta', '0013_auto_20151117_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokument',
            name='delovninalog',
            field=models.ForeignKey(to='delovninalogi.DelovniNalog', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dokument',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek', null=True, blank=True),
        ),
    ]
