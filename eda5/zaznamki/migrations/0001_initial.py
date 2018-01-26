# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('reklamacije', '0001_initial'),
        ('dogodki', '0001_initial'),
        ('povprasevanje', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('razdelilnik', '0001_initial'),
        ('sestanki', '0001_initial'),
        ('skladisce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zaznamek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                'verbose_name_plural': 'Zaznamki',
                'verbose_name': 'Zaznamek',
            },
        ),
    ]
