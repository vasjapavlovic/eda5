# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zaznamek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tekst', models.TextField(verbose_name='Tekst')),
                ('datum', models.DateField(verbose_name='Datum')),
                ('ura', models.TimeField(verbose_name='Ura')),
                ('delovninalog', models.ForeignKey(to='delovninalogi.DelovniNalog', null=True, blank=True)),
                ('zahtevek', models.ForeignKey(to='zahtevki.Zahtevek', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Zaznamek',
                'verbose_name_plural': 'Zaznamki',
            },
        ),
    ]
