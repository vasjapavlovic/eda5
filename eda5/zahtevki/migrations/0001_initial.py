# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0002_auto_20180104_1543'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zahtevek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('vrsta', models.IntegerField(choices=[(1, 'Škodni Dogodek'), (2, 'Sestanek'), (3, 'Izvedba del'), (4, 'Predaja Lastnine'), (5, 'Analiza Zahtevka'), (6, 'Povpraševanje'), (7, 'Reklamacija')])),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('zahtevek_parent', models.ForeignKey(null=True, blank=True, verbose_name='Zahtevek Parent', to='zahtevki.Zahtevek')),
                ('zahtevek_povezava', models.ManyToManyField(verbose_name='Povezava zahtevkov', to='zahtevki.Zahtevek', blank=True, related_name='_zahtevek_povezava_+')),
            ],
            options={
                'verbose_name': 'zahtevek',
                'ordering': ('-pk',),
                'verbose_name_plural': 'zahtevki',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekAnaliza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZahtevekIzvedbaDela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_zakonska_obveza', models.NullBooleanField(verbose_name='zakonska obveza')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'izvedba dela',
                'ordering': ('-zahtevek__oznaka',),
                'verbose_name_plural': 'izvedba del',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekPovprasevanje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZahtevekReklamacija',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZahtevekSestanek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('datum', models.DateField(null=True, blank=True)),
                ('sklicatelj', models.ForeignKey(null=True, blank=True, to='partnerji.Partner')),
                ('udelezenci', models.ManyToManyField(verbose_name='udeleženci', to='partnerji.Oseba', blank=True)),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'sestanek',
                'ordering': ('-zahtevek__oznaka',),
                'verbose_name_plural': 'sestanki',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSkodniDogodek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('datum_nastanka_skode', models.DateField(verbose_name='datum nastanka škode', null=True, blank=True)),
                ('vzrok_skode', models.TextField(verbose_name='vzrok škode', blank=True)),
                ('is_prijava_policiji', models.NullBooleanField(verbose_name='prijavljeno policiji')),
                ('povzrocitelj', models.CharField(verbose_name='povzročitelj (opisno)', max_length=255, blank=True)),
                ('predvidena_visina_skode', models.DecimalField(verbose_name='predvidena višina škode', decimal_places=2, null=True, blank=True, max_digits=7)),
                ('poskodovane_stvari', models.ManyToManyField(to='deli.Element', blank=True)),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'škodni dogodek',
                'ordering': ('datum_nastanka_skode',),
                'verbose_name_plural': 'škodni dogodki',
            },
        ),
    ]
