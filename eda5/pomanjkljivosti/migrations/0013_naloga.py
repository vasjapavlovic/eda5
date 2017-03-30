# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0011_auto_20170330_1450'),
        ('partnerji', '0012_auto_20170302_0706'),
        ('pomanjkljivosti', '0012_pomanjkljivost_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naloga',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv pomanjkljivosti')),
                ('opis', models.TextField(null=True, blank=True, verbose_name='opis pomanjkljivosti')),
                ('datum', models.DateField(verbose_name='datum')),
                ('rok', models.DateField(verbose_name='rok za izvedbo')),
                ('oseba', models.ManyToManyField(to='partnerji.Oseba', verbose_name='Za Osebe')),
                ('zahtevek', models.ForeignKey(blank=True, verbose_name='zahtevek', null=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'naloga',
                'verbose_name_plural': 'naloge',
            },
        ),
    ]
