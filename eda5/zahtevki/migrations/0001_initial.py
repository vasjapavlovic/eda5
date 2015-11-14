# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('narocila', '0001_initial'),
        ('deli', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zahtevek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0)),
                ('oznaka', models.CharField(max_length=20)),
                ('predmet', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_zakonska_obveza', models.BooleanField(verbose_name='zakonska obveza')),
            ],
            options={
                'verbose_name': 'izvedba dela',
                'verbose_name_plural': 'izvedba del',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSestanek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('datum', models.DateField()),
                ('sklicatelj', models.ForeignKey(to='partnerji.Partner')),
                ('udelezenci', models.ManyToManyField(to='partnerji.Oseba', verbose_name='udeleženci')),
                ('zapisnik', models.ForeignKey(to='posta.Dokument', null=True, blank=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('datum_nastanka_skode', models.DateField(verbose_name='datum nastanka škdoe')),
                ('vzrok_skode', models.TextField(verbose_name='vzrok škode', blank=True)),
                ('is_prijava_policiji', models.BooleanField(verbose_name='prijavljeno policiji')),
                ('povzrocitelj', models.CharField(max_length=255, verbose_name='povzročitelj', blank=True)),
                ('predvidena_visina_skode', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='predvidena višina škode', blank=True, null=True)),
                ('dokazno_gradivo', models.ForeignKey(to='posta.Dokument', related_name='dokazno_gradivo', null=True, blank=True)),
                ('dokument_poravnava', models.ForeignKey(related_name='dokument_poravnava', verbose_name='poravnava škode', to='posta.Dokument', null=True, blank=True)),
                ('dokument_prijava_skode', models.ForeignKey(related_name='dokument_prijava_skode', verbose_name='prijava škode', to='posta.Dokument', null=True, blank=True)),
                ('dokument_zapisnik_ogleda', models.ForeignKey(related_name='dokument_zapisnik_ogleda', verbose_name='zapisnik o ogledu škode', to='posta.Dokument', null=True, blank=True)),
                ('poskodovane_stvari', models.ManyToManyField(to='deli.Element', blank=True)),
            ],
            options={
                'verbose_name': 'škodni dogodek',
                'ordering': ('datum_nastanka_skode',),
                'verbose_name_plural': 'škodni dogodki',
            },
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_izvedba_dela',
            field=models.OneToOneField(to='zahtevki.ZahtevekIzvedbaDela', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_parent',
            field=models.ForeignKey(to='zahtevki.Zahtevek', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_sestanek',
            field=models.OneToOneField(to='zahtevki.ZahtevekSestanek', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_skodni_dogodek',
            field=models.OneToOneField(to='zahtevki.ZahtevekSkodniDogodek', null=True, blank=True),
        ),
    ]
