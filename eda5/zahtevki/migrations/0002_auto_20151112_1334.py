# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zahtevek',
            name='dokument',
            field=models.ManyToManyField(to='posta.Dokument', blank=True),
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
