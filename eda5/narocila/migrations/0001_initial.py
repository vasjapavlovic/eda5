# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0008_auto_20151026_0727'),
        ('partnerji', '0012_partner_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Narocilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=20)),
                ('predmet', models.CharField(verbose_name='predmet', max_length=255)),
                ('datum_narocila', models.DateField(verbose_name='datum naročila')),
                ('datum_veljavnosti', models.DateField(verbose_name='velja do')),
                ('vrednost', models.DecimalField(max_digits=7, decimal_places=2)),
                ('dodatna_dokumentacija', models.ManyToManyField(to='posta.Dokument')),
                ('izvajalec', models.ForeignKey(related_name='izvajalec', to='partnerji.Partner')),
            ],
            options={
                'verbose_name': 'Naročilo',
                'verbose_name_plural': 'Naročila',
            },
        ),
        migrations.CreateModel(
            name='NarociloPogodba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('st_pogodbe', models.CharField(verbose_name='številka pogodbe', max_length=20)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
            field=models.OneToOneField(to='narocila.NarociloPogodba'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocilo_telefon',
            field=models.OneToOneField(to='narocila.NarociloTelefon'),
        ),
        migrations.AddField(
            model_name='narocilo',
            name='narocnik',
            field=models.ForeignKey(related_name='narocnik', to='partnerji.Partner'),
        ),
    ]
