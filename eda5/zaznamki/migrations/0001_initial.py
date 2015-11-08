# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0008_zahtevek_zahtevek_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zaznamek',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tekst', models.TextField(verbose_name='Tekst')),
                ('datum', models.DateField(verbose_name='Datum')),
                ('ura', models.TimeField(verbose_name='Ura')),
                ('zahtevek', models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'Zaznamek',
                'verbose_name_plural': 'Zaznamki',
            },
        ),
    ]
