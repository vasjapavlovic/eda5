# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zahtevek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('vrsta', models.IntegerField(choices=[(1, 'Škodni Dogodek'), (2, 'Sestanek'), (3, 'Izvedba del'), (4, 'Predaja Lastnine'), (5, 'Analiza Zahtevka'), (6, 'Povpraševanje'), (7, 'Reklamacija')])),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('zahtevek_parent', models.ForeignKey(null=True, verbose_name='Zahtevek Parent', blank=True, to='zahtevki.Zahtevek')),
                ('zahtevek_povezava', models.ManyToManyField(blank=True, to='zahtevki.Zahtevek', related_name='_zahtevek_povezava_+', verbose_name='Povezava zahtevkov')),
            ],
            options={
                'verbose_name_plural': 'zahtevki',
                'verbose_name': 'zahtevek',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='ZahtevekAnaliza',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ZahtevekIzvedbaDela',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_zakonska_obveza', models.NullBooleanField(verbose_name='zakonska obveza')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'izvedba del',
                'verbose_name': 'izvedba dela',
                'ordering': ('-zahtevek__oznaka',),
            },
        ),
        migrations.CreateModel(
            name='ZahtevekPovprasevanje',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ZahtevekReklamacija',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ZahtevekSestanek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('datum', models.DateField(blank=True, null=True)),
                ('sklicatelj', models.ForeignKey(null=True, blank=True, to='partnerji.Partner')),
                ('udelezenci', models.ManyToManyField(blank=True, to='partnerji.Oseba', verbose_name='udeleženci')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'sestanki',
                'verbose_name': 'sestanek',
                'ordering': ('-zahtevek__oznaka',),
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSkodniDogodek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('datum_nastanka_skode', models.DateField(blank=True, null=True, verbose_name='datum nastanka škode')),
                ('vzrok_skode', models.TextField(blank=True, verbose_name='vzrok škode')),
                ('is_prijava_policiji', models.NullBooleanField(verbose_name='prijavljeno policiji')),
                ('povzrocitelj', models.CharField(blank=True, max_length=255, verbose_name='povzročitelj (opisno)')),
                ('predvidena_visina_skode', models.DecimalField(blank=True, max_digits=7, decimal_places=2, null=True, verbose_name='predvidena višina škode')),
                ('poskodovane_stvari', models.ManyToManyField(blank=True, to='deli.Element')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'škodni dogodki',
                'verbose_name': 'škodni dogodek',
                'ordering': ('datum_nastanka_skode',),
            },
        ),
    ]
