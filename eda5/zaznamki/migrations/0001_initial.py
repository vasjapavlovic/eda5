# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('delovninalogi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zaznamek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tekst', models.TextField(verbose_name='Tekst')),
                ('datum', models.DateField(verbose_name='Datum')),
                ('ura', models.TimeField(verbose_name='Ura')),
                ('delovninalog', models.ForeignKey(to='delovninalogi.DelovniNalog', blank=True, null=True)),
                ('zahtevek', models.ForeignKey(to='zahtevki.Zahtevek', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Zaznamki',
                'verbose_name': 'Zaznamek',
            },
        ),
    ]
