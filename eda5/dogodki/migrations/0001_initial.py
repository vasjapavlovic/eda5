# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0006_auto_20161031_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogodek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('datum_dogodka', models.DateField(verbose_name='datum dogodka')),
                ('opis_dogodka', models.TextField(verbose_name='opis dogodka')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
