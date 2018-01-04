# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('delovninalogi', '0002_vzorecopravila_narocilo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reklamacija',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
                ('datum', models.DateField(verbose_name='datum vložene reklamacije')),
                ('okvirni_strosek', models.DecimalField(verbose_name='Okvirni Strošek Reklamacije', decimal_places=2, max_digits=7)),
                ('delovninalog', models.ForeignKey(null=True, blank=True, verbose_name='delovninalog', to='delovninalogi.DelovniNalog')),
                ('izvajalec', models.ForeignKey(verbose_name='izvajalec', to='partnerji.Partner', related_name='reklamacija_izvajalec')),
                ('narocnik', models.ForeignKey(verbose_name='naročnik', to='partnerji.Partner', related_name='reklamacija_narocnik')),
                ('zahtevek', models.ForeignKey(null=True, blank=True, verbose_name='zahtevek', to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'Reklamacije',
            },
        ),
    ]
