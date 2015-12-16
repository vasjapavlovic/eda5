# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('narocila', '0001_initial'),
        ('deli', '0002_auto_20151215_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zahtevek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0)),
                ('oznaka', models.CharField(max_length=20)),
                ('vrsta', models.IntegerField(choices=[(1, 'Škodni Dogodek'), (2, 'Sestanek'), (3, 'Izvedba del')])),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('zahtevek_parent', models.ForeignKey(to='zahtevki.Zahtevek', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'zahtevki',
                'verbose_name': 'zahtevek',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='ZahtevekIzvedbaDela',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_zakonska_obveza', models.NullBooleanField(verbose_name='zakonska obveza')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'izvedba del',
                'verbose_name': 'izvedba dela',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSestanek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('datum', models.DateField(blank=True, null=True)),
                ('sklicatelj', models.ForeignKey(to='partnerji.Partner', blank=True, null=True)),
                ('udelezenci', models.ManyToManyField(blank=True, to='partnerji.Oseba', verbose_name='udeleženci')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'sestanki',
                'verbose_name': 'sestanek',
                'ordering': ('datum',),
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSkodniDogodek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('datum_nastanka_skode', models.DateField(blank=True, null=True, verbose_name='datum nastanka škode')),
                ('vzrok_skode', models.TextField(blank=True, verbose_name='vzrok škode')),
                ('is_prijava_policiji', models.NullBooleanField(verbose_name='prijavljeno policiji')),
                ('povzrocitelj', models.CharField(blank=True, max_length=255, verbose_name='povzročitelj (opisno)')),
                ('predvidena_visina_skode', models.DecimalField(max_digits=7, blank=True, decimal_places=2, null=True, verbose_name='predvidena višina škode')),
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
