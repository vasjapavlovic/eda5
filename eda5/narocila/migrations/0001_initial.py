# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0002_auto_20171209_2221'),
        ('posta', '__first__'),
        ('zahtevki', '__first__'),
        ('partnerji', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Narocilo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('predmet', models.CharField(max_length=255)),
                ('datum_narocila', models.DateField(verbose_name='datum naročila')),
                ('datum_veljavnosti', models.DateField(verbose_name='velja do')),
                ('vrednost', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=7)),
                ('izvajalec', models.ForeignKey(to='partnerji.Partner', related_name='izvajalec')),
            ],
            options={
                'verbose_name': 'naročilo',
                'ordering': ('-id',),
                'verbose_name_plural': 'naročila',
            },
        ),
        migrations.CreateModel(
            name='NarociloDokument',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('dokument', models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje')),
                ('narocilo', models.OneToOneField(null=True, to='narocila.Narocilo', blank=True)),
                ('vrsta_dokumenta', models.ForeignKey(verbose_name='vrsta dokumenta', to='posta.VrstaDokumenta')),
            ],
            options={
                'verbose_name': 'naročilo z dokumentom',
                'verbose_name_plural': 'naročilo z dokumentom',
            },
        ),
        migrations.CreateModel(
            name='NarociloTelefon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('dogovor_text', models.CharField(verbose_name='opis dogovora', max_length=255)),
                ('dogovor_date', models.DateField(verbose_name='datum dogovora')),
                ('dogovor_time', models.TimeField(verbose_name='čas dogovora')),
                ('dogovor_person', models.CharField(null=True, verbose_name='Oseba s katero si se dogovarjal', blank=True, max_length=255)),
                ('dogovor_phonenumber', models.CharField(null=True, verbose_name='telefonska številka', blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'ustno/telefonsko naročilo',
                'verbose_name_plural': 'naročila po telefonu',
            },
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(null=True, to='narocila.NarociloTelefon', blank=True),
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
