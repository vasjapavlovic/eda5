# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('racunovodstvo', '0001_initial'),
        ('etaznalastnina', '0001_initial'),
        ('core', '0001_initial'),
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Razdelilnik',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(blank=True, max_length=20, null=True)),
                ('oznaka_gen', models.CharField(blank=True, max_length=20, null=True)),
                ('naziv', models.CharField(max_length=255)),
                ('obdobje_obracuna_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_obracuna_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
                ('stavba', models.ForeignKey(to='deli.Stavba')),
                ('zahtevek', models.ForeignKey(null=True, verbose_name='zahtevek', blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'Razdelilniki',
                'verbose_name': 'Razdelilnik',
                'ordering': ('-obdobje_obracuna_leto', '-obdobje_obracuna_mesec'),
            },
        ),
        migrations.CreateModel(
            name='StrosekDelitevVrsta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('skrajsan_naziv', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Vrsta delitve stroška',
                'verbose_name': 'Vrsta delitve stroška',
            },
        ),
        migrations.CreateModel(
            name='StrosekKljucDelitve',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('skrajsan_naziv', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Ključ delitve stroška',
                'verbose_name': 'Ključ delitve stroška',
            },
        ),
        migrations.CreateModel(
            name='StrosekLE',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('delilnik_vrednost', models.DecimalField(max_digits=8, decimal_places=4)),
                ('lastniska_enota_interna', models.ForeignKey(to='etaznalastnina.LastniskaEnotaInterna')),
            ],
            options={
                'verbose_name_plural': 'stroški na LE',
                'verbose_name': 'strošek na LE',
            },
        ),
        migrations.CreateModel(
            name='StrosekRazdelilnik',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_razdeljen', models.BooleanField(default=False)),
                ('razdeljen_datum', models.DateField(blank=True, null=True)),
                ('razdelilnik', models.ForeignKey(to='razdelilnik.Razdelilnik')),
                ('strosek', models.OneToOneField(to='racunovodstvo.Strosek')),
            ],
            options={
                'verbose_name_plural': 'StrosekRazdelilnik',
                'verbose_name': 'StrosekRazdelilnik',
            },
        ),
        migrations.CreateModel(
            name='StrosekRazdelilnikPostavka',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('delilnik_vrednost', models.DecimalField(max_digits=8, decimal_places=4)),
                ('is_strosek_posameznidel', models.NullBooleanField(verbose_name='strosek na posameznem delu')),
                ('delilnik_kljuc', models.ForeignKey(null=True, blank=True, to='razdelilnik.StrosekKljucDelitve')),
                ('delitev_vrsta', models.ForeignKey(null=True, blank=True, to='razdelilnik.StrosekDelitevVrsta')),
                ('lastniska_skupina', models.ForeignKey(null=True, blank=True, to='etaznalastnina.LastniskaSkupina')),
                ('strosek_razdelilnik', models.ForeignKey(to='razdelilnik.StrosekRazdelilnik')),
            ],
            options={
                'verbose_name_plural': 'StrosekRazdelilnikPostavke',
                'verbose_name': 'StrosekRazdelilnikPostavka',
                'ordering': ('oznaka',),
            },
        ),
        migrations.AddField(
            model_name='strosekle',
            name='strosek_razdelilnik',
            field=models.ForeignKey(to='razdelilnik.StrosekRazdelilnik'),
        ),
    ]
