# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '__first__'),
        ('racunovodstvo', '__first__'),
        ('partnerji', '__first__'),
        ('reklamacije', '__first__'),
        ('deli', '__first__'),
        ('posta', '__first__'),
        ('skladisce', '__first__'),
        ('delovninalogi', '__first__'),
        ('katalog', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arhiv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(unique=True, verbose_name='oznaka', max_length=50)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
            ],
            options={
                'verbose_name': 'arhiv',
                'verbose_name_plural': 'arhivi',
            },
        ),
        migrations.CreateModel(
            name='Arhiviranje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('elektronski', models.BooleanField(default=True, verbose_name='elektronski hramba')),
                ('fizicni', models.BooleanField(default=False, verbose_name='fizični hramba')),
                ('arhiviral', models.ForeignKey(to='partnerji.Oseba')),
                ('artikel', models.ForeignKey(to='katalog.ModelArtikla', null=True, blank=True)),
                ('delovninalog', models.ForeignKey(to='delovninalogi.DelovniNalog', null=True, blank=True)),
                ('delstavbe', models.ForeignKey(to='deli.DelStavbe', null=True, blank=True)),
                ('dobava', models.ForeignKey(to='skladisce.Dobava', null=True, blank=True)),
                ('dokument', models.OneToOneField(null=True, to='posta.Dokument', blank=True)),
                ('element', models.ForeignKey(to='deli.Element', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'arhiviranje',
                'verbose_name_plural': 'arhiviranje',
            },
        ),
        migrations.CreateModel(
            name='ArhivMesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=50)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('arhiv', models.ForeignKey(to='arhiv.Arhiv')),
                ('zahtevek', models.OneToOneField(null=True, to='zahtevki.Zahtevek', blank=True)),
            ],
            options={
                'verbose_name': 'arhivsko mesto',
                'verbose_name_plural': 'arhivska mesta',
            },
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='lokacija_hrambe',
            field=models.ForeignKey(null=True, to='arhiv.ArhivMesto', blank=True, verbose_name='lokacija hrambe'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='racun',
            field=models.OneToOneField(null=True, to='racunovodstvo.Racun', blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='reklamacija',
            field=models.ForeignKey(to='reklamacije.Reklamacija', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='sestanek',
            field=models.ForeignKey(to='sestanki.Sestanek', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek', null=True, blank=True),
        ),
    ]
