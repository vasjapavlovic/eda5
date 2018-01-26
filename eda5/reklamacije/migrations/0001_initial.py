# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reklamacija',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
                ('datum', models.DateField(verbose_name='datum vložene reklamacije')),
                ('okvirni_strosek', models.DecimalField(verbose_name='Okvirni Strošek Reklamacije', max_digits=7, decimal_places=2)),
                ('delovninalog', models.ForeignKey(null=True, verbose_name='delovninalog', blank=True, to='delovninalogi.DelovniNalog')),
                ('izvajalec', models.ForeignKey(related_name='reklamacija_izvajalec', verbose_name='izvajalec', to='partnerji.Partner')),
                ('narocnik', models.ForeignKey(related_name='reklamacija_narocnik', verbose_name='naročnik', to='partnerji.Partner')),
                ('zahtevek', models.ForeignKey(null=True, verbose_name='zahtevek', blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'Reklamacije',
            },
        ),
    ]
