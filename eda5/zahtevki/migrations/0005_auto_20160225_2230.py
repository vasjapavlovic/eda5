# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0004_auto_20160102_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZahtevekAnaliza',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZahtevekPovprasevanje',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZahtevekReklamacija',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='zahtevek',
            name='vrsta',
            field=models.IntegerField(choices=[(1, 'Škodni Dogodek'), (2, 'Sestanek'), (3, 'Izvedba del'), (4, 'Predaja Lastnine'), (5, 'Analiza Zahtevka'), (6, 'Povpraševanje'), (7, 'Reklamacija')]),
        ),
    ]
