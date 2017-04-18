# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skladisce', '__first__'),
        ('sestanki', '0003_auto_20170410_1800'),
        ('povprasevanje', '__first__'),
        ('delovninalogi', '__first__'),
        ('zahtevki', '__first__'),
        ('reklamacije', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zaznamek',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('tekst', models.TextField(verbose_name='Tekst')),
                ('datum', models.DateField(verbose_name='Datum')),
                ('ura', models.TimeField(verbose_name='Ura')),
                ('delovninalog', models.ForeignKey(null=True, blank=True, to='delovninalogi.DelovniNalog')),
                ('dobava', models.ForeignKey(null=True, blank=True, to='skladisce.Dobava')),
                ('povprasevanje', models.ForeignKey(null=True, blank=True, to='povprasevanje.Povprasevanje')),
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
