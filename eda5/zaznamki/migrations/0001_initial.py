# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '__first__'),
        ('reklamacije', '__first__'),
        ('povprasevanje', '__first__'),
        ('dogodki', '__first__'),
        ('skladisce', '__first__'),
        ('sestanki', '__first__'),
        ('razdelilnik', '0001_initial'),
        ('delovninalogi', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zaznamek',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tekst', models.TextField(verbose_name='Tekst')),
                ('datum', models.DateField(verbose_name='Datum')),
                ('ura', models.TimeField(verbose_name='Ura')),
                ('delovninalog', models.ForeignKey(null=True, blank=True, to='delovninalogi.DelovniNalog')),
                ('dobava', models.ForeignKey(null=True, blank=True, to='skladisce.Dobava')),
                ('dogodek', models.ForeignKey(null=True, blank=True, to='dogodki.Dogodek')),
                ('povprasevanje', models.ForeignKey(null=True, blank=True, to='povprasevanje.Povprasevanje')),
                ('razdelilnik', models.ForeignKey(null=True, blank=True, to='razdelilnik.Razdelilnik')),
                ('reklamacija', models.ForeignKey(null=True, blank=True, to='reklamacije.Reklamacija')),
                ('sestanek', models.ForeignKey(null=True, blank=True, to='sestanki.Sestanek')),
                ('zahtevek', models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'Zaznamek',
                'verbose_name_plural': 'Zaznamki',
            },
        ),
    ]
