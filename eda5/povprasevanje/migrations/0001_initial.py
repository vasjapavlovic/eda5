# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ponudba',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('garancija', models.CharField(blank=True, max_length=255, null=True, verbose_name='garancija - opisno')),
                ('referenca_opis', models.CharField(blank=True, max_length=255, null=True, verbose_name='referenca - opisno')),
                ('ponudba_dokument', models.ForeignKey(related_name='ponudba_dokument', null=True, verbose_name='ponudba dokument', blank=True, to='arhiv.Arhiviranje')),
                ('ponudnik', models.ForeignKey(verbose_name='ponudnik', to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'ponudbe',
            },
        ),
        migrations.CreateModel(
            name='PonudbaPoPostavki',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('vrednost_za_izracun', models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True, verbose_name='vrednost-izračun cene')),
                ('vrednost_opis', models.CharField(blank=True, max_length=255, null=True, verbose_name='vrednost-opisno')),
                ('ponudba', models.ForeignKey(to='povprasevanje.Ponudba')),
            ],
            options={
                'verbose_name_plural': 'ponudbe po postavkah',
            },
        ),
        migrations.CreateModel(
            name='Postavka',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
            ],
            options={
                'verbose_name_plural': 'postavke povpraševanja',
            },
        ),
        migrations.CreateModel(
            name='Povprasevanje',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
                ('datum', models.DateField(verbose_name='datum')),
                ('priloge', models.ManyToManyField(blank=True, to='arhiv.Arhiviranje', related_name='povprasevanje_priloge', verbose_name='priloge')),
                ('zahtevek', models.ForeignKey(null=True, verbose_name='zahtevek', blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'povpraševanja',
            },
        ),
        migrations.AddField(
            model_name='postavka',
            name='povprasevanje',
            field=models.ForeignKey(verbose_name='povprasevanje', to='povprasevanje.Povprasevanje'),
        ),
        migrations.AddField(
            model_name='postavka',
            name='priloge',
            field=models.ManyToManyField(blank=True, to='arhiv.Arhiviranje', related_name='postavka_priloge', verbose_name='priloge'),
        ),
        migrations.AddField(
            model_name='ponudbapopostavki',
            name='postavka',
            field=models.ForeignKey(to='povprasevanje.Postavka'),
        ),
        migrations.AddField(
            model_name='ponudba',
            name='povprasevanje',
            field=models.ForeignKey(verbose_name='povprasevanje', to='povprasevanje.Povprasevanje'),
        ),
        migrations.AddField(
            model_name='ponudba',
            name='referenca_dokument',
            field=models.ForeignKey(related_name='referenca_dokument', null=True, verbose_name='referenca - dokumentacija', blank=True, to='arhiv.Arhiviranje'),
        ),
        migrations.AddField(
            model_name='ponudba',
            name='vrednost_postavke',
            field=models.ManyToManyField(blank=True, to='povprasevanje.Postavka', through='povprasevanje.PonudbaPoPostavki', verbose_name='vrednost postavke'),
        ),
        migrations.AlterUniqueTogether(
            name='ponudbapopostavki',
            unique_together=set([('postavka', 'ponudba')]),
        ),
    ]
