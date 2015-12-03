# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('deli', '0002_auto_20151203_0301'),
        ('narocila', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zahtevek',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0)),
                ('oznaka', models.CharField(max_length=20)),
                ('vrsta', models.IntegerField(choices=[(1, 'Škodni Dogodek'), (2, 'Sestanek'), (3, 'Izvedba del')])),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('zahtevek_parent', models.ForeignKey(to='zahtevki.Zahtevek', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'zahtevek',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'zahtevki',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekIzvedbaDela',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datum', models.DateField(null=True, blank=True)),
                ('sklicatelj', models.ForeignKey(to='partnerji.Partner', null=True, blank=True)),
                ('udelezenci', models.ManyToManyField(verbose_name='udeleženci', to='partnerji.Oseba', blank=True)),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'sestanek',
                'ordering': ('datum',),
                'verbose_name_plural': 'sestanki',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSkodniDogodek',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datum_nastanka_skode', models.DateField(verbose_name='datum nastanka škode', null=True, blank=True)),
                ('vzrok_skode', models.TextField(verbose_name='vzrok škode', blank=True)),
                ('is_prijava_policiji', models.NullBooleanField(verbose_name='prijavljeno policiji')),
                ('povzrocitelj', models.CharField(verbose_name='povzročitelj (opisno)', max_length=255, blank=True)),
                ('predvidena_visina_skode', models.DecimalField(verbose_name='predvidena višina škode', null=True, max_digits=7, decimal_places=2, blank=True)),
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
