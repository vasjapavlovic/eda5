# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0010_auto_20170214_1533'),
        ('delovninalogi', '0016_opravilo_status'),
        ('partnerji', '0012_auto_20170302_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reklamacija',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=255, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('opis', models.TextField(verbose_name='opis')),
                ('datum', models.DateField(verbose_name='datum vložene reklamacije')),
                ('okvirni_strosek', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Okvirni Strošek Reklamacije')),
                ('delovninalog', models.ForeignKey(to='delovninalogi.DelovniNalog', null=True, blank=True, verbose_name='delovninalog')),
                ('izvajalec', models.ForeignKey(related_name='reklamacija_izvajalec', verbose_name='izvajalec', to='partnerji.Partner')),
                ('narocnik', models.ForeignKey(related_name='reklamacija_narocnik', verbose_name='naročnik', to='partnerji.Partner')),
                ('zahtevek', models.ForeignKey(to='zahtevki.Zahtevek', null=True, blank=True, verbose_name='zahtevek')),
            ],
            options={
                'verbose_name_plural': 'Reklamacije',
            },
        ),
    ]
