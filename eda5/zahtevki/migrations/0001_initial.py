# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0008_auto_20151026_0727'),
        ('narocila', '0006_auto_20151101_1428'),
        ('partnerji', '0013_auto_20151030_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zahtevek',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('predmet', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'ordering': ('oznaka',),
                'verbose_name': 'zahtevek',
                'verbose_name_plural': 'zahtevki',
            },
        ),
        migrations.CreateModel(
            name='ZahtevekSkodniDogodek',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('dokument_poravnava', models.ForeignKey(to='posta.Dokument', related_name='dokument_poravnava', verbose_name='poravnava škode')),
                ('dokument_prijava_skode', models.ForeignKey(to='posta.Dokument', related_name='dokument_prijava_skode', verbose_name='prijava škode')),
                ('dokument_zapisnik_ogleda', models.ForeignKey(to='posta.Dokument', related_name='dokument_zapisnik_ogleda', verbose_name='zapisnik o ogledu škode')),
            ],
            options={
                'verbose_name': 'škodni dogodek',
                'verbose_name_plural': 'škodni dogodki',
            },
        ),
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_skodni_dogodek',
            field=models.OneToOneField(to='zahtevki.ZahtevekSkodniDogodek'),
        ),
    ]
