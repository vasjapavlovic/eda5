# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Narocilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('predmet', models.CharField(max_length=255)),
                ('datum_narocila', models.DateField(verbose_name='datum naročila')),
                ('datum_veljavnosti', models.DateField(verbose_name='velja do')),
                ('vrednost', models.DecimalField(blank=True, max_digits=7, null=True, decimal_places=2)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('dokument', models.ForeignKey(blank=True, to='arhiv.Arhiviranje', null=True)),
                ('narocilo', models.OneToOneField(blank=True, to='narocila.Narocilo', null=True)),
            ],
            options={
                'verbose_name': 'naročilo z dokumentom',
                'verbose_name_plural': 'naročilo z dokumentom',
            },
        ),
        migrations.CreateModel(
            name='NarociloTelefon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('dogovor_text', models.CharField(verbose_name='opis dogovora', max_length=255)),
                ('dogovor_date', models.DateField(verbose_name='datum dogovora')),
                ('dogovor_time', models.TimeField(verbose_name='čas dogovora')),
                ('dogovor_person', models.CharField(verbose_name='Oseba s katero si se dogovarjal', blank=True, null=True, max_length=255)),
                ('dogovor_phonenumber', models.CharField(verbose_name='telefonska številka', blank=True, null=True, max_length=255)),
            ],
            options={
                'verbose_name': 'ustno/telefonsko naročilo',
                'verbose_name_plural': 'naročila po telefonu',
            },
        ),
    ]
