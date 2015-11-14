# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Narocilo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('predmet', models.CharField(max_length=255)),
                ('datum_narocila', models.DateField(verbose_name='datum naročila')),
                ('datum_veljavnosti', models.DateField(verbose_name='velja do')),
                ('vrednost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dodatna_dokumentacija', models.ManyToManyField(to='posta.Dokument', blank=True)),
                ('izvajalec', models.ForeignKey(related_name='izvajalec', to='partnerji.Partner')),
            ],
            options={
                'verbose_name': 'naročilo',
                'verbose_name_plural': 'naročila',
            },
        ),
        migrations.CreateModel(
            name='NarociloPogodba',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('st_pogodbe', models.CharField(max_length=20, verbose_name='številka pogodbe')),
                ('predmet_pogodbe', models.CharField(max_length=255, verbose_name='številka pogodbe')),
                ('pogodba', models.ForeignKey(to='posta.Dokument')),
            ],
            options={
                'verbose_name': 'pogodbeno naročilo',
                'verbose_name_plural': 'pogodbena naročila',
            },
        ),
        migrations.CreateModel(
            name='NarociloTelefon',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('telefonska_stevilka', models.CharField(max_length=20)),
                ('datum_klica', models.DateField()),
                ('cas_klica', models.TimeField()),
                ('telefonsko_sporocilo', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'naročilo po telefonu',
                'verbose_name_plural': 'naročila po telefonu',
            },
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_pogodba',
            field=models.OneToOneField(to='narocila.NarociloPogodba', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(to='narocila.NarociloTelefon', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocnik',
            field=models.ForeignKey(related_name='narocnik', to='partnerji.SkupinaPartnerjev'),
        ),
    ]
