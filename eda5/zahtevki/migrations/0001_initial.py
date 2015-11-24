# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('deli', '0002_auto_20151122_2204'),
        ('narocila', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zahtevek',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('vrsta', models.IntegerField(choices=[(1, 'Škodni Dogodek'), (2, 'Sestanek'), (3, 'Izvedba del')])),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('zahtevek_parent', models.ForeignKey(null=True, to='zahtevki.Zahtevek', blank=True)),
            ],
            options={
                'verbose_name': 'zahtevek',
                'verbose_name_plural': 'zahtevki',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='ZahtevekIzvedbaDela',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_zakonska_obveza', models.NullBooleanField(verbose_name='zakonska obveza')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'izvedba dela',
                'verbose_name_plural': 'izvedba del',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSestanek',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(blank=True, null=True)),
                ('sklicatelj', models.ForeignKey(null=True, to='partnerji.Partner', blank=True)),
                ('udelezenci', models.ManyToManyField(verbose_name='udeleženci', to='partnerji.Oseba', blank=True)),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'sestanek',
                'verbose_name_plural': 'sestanki',
                'ordering': ('datum',),
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSkodniDogodek',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('datum_nastanka_skode', models.DateField(verbose_name='datum nastanka škode', blank=True, null=True)),
                ('vzrok_skode', models.TextField(verbose_name='vzrok škode', blank=True)),
                ('is_prijava_policiji', models.NullBooleanField(verbose_name='prijavljeno policiji')),
                ('povzrocitelj', models.CharField(max_length=255, blank=True, verbose_name='povzročitelj (opisno)')),
                ('predvidena_visina_skode', models.DecimalField(max_digits=7, verbose_name='predvidena višina škode', blank=True, null=True, decimal_places=2)),
                ('poskodovane_stvari', models.ManyToManyField(to='deli.Element', blank=True)),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'škodni dogodek',
                'verbose_name_plural': 'škodni dogodki',
                'ordering': ('datum_nastanka_skode',),
            },
        ),
    ]
