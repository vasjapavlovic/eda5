# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Narocilo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('predmet', models.CharField(max_length=255)),
                ('datum_narocila', models.DateField(verbose_name='datum naročila')),
                ('datum_veljavnosti', models.DateField(verbose_name='velja do')),
                ('vrednost', models.DecimalField(blank=True, max_digits=7, null=True, decimal_places=2)),
                ('izvajalec', models.ForeignKey(to='partnerji.Partner', related_name='izvajalec')),
            ],
            options={
                'verbose_name_plural': 'naročila',
                'verbose_name': 'naročilo',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='NarociloDokument',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('dokument', models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje')),
                ('narocilo', models.OneToOneField(null=True, blank=True, to='narocila.Narocilo')),
                ('vrsta_dokumenta', models.ForeignKey(verbose_name='vrsta dokumenta', to='posta.VrstaDokumenta')),
            ],
            options={
                'verbose_name_plural': 'naročilo z dokumentom',
                'verbose_name': 'naročilo z dokumentom',
            },
        ),
        migrations.CreateModel(
            name='NarociloTelefon',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('dogovor_text', models.CharField(verbose_name='opis dogovora', max_length=255)),
                ('dogovor_date', models.DateField(verbose_name='datum dogovora')),
                ('dogovor_time', models.TimeField(verbose_name='čas dogovora')),
                ('dogovor_person', models.CharField(blank=True, max_length=255, null=True, verbose_name='Oseba s katero si se dogovarjal')),
                ('dogovor_phonenumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='telefonska številka')),
            ],
            options={
                'verbose_name_plural': 'naročila po telefonu',
                'verbose_name': 'ustno/telefonsko naročilo',
            },
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(null=True, blank=True, to='narocila.NarociloTelefon'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocnik',
            field=models.ForeignKey(to='partnerji.Partner', related_name='narocnik'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
