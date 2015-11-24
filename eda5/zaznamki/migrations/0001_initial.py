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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tekst', models.TextField(verbose_name='Tekst')),
                ('datum', models.DateField(verbose_name='Datum')),
                ('ura', models.TimeField(verbose_name='Ura')),
                ('delovninalog', models.ForeignKey(null=True, to='delovninalogi.DelovniNalog', blank=True)),
                ('zahtevek', models.ForeignKey(null=True, to='zahtevki.Zahtevek', blank=True)),
            ],
            options={
                'verbose_name': 'Zaznamek',
                'verbose_name_plural': 'Zaznamki',
            },
        ),
    ]
