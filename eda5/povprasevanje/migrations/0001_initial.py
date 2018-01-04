# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ponudba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('garancija', models.CharField(verbose_name='garancija - opisno', max_length=255, null=True, blank=True)),
                ('referenca_opis', models.CharField(verbose_name='referenca - opisno', max_length=255, null=True, blank=True)),
                ('ponudba_dokument', models.ForeignKey(null=True, blank=True, verbose_name='ponudba dokument', to='arhiv.Arhiviranje', related_name='ponudba_dokument')),
                ('ponudnik', models.ForeignKey(verbose_name='ponudnik', to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'ponudbe',
            },
        ),
        migrations.CreateModel(
            name='PonudbaPoPostavki',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('vrednost_za_izracun', models.DecimalField(verbose_name='vrednost-izračun cene', decimal_places=2, null=True, blank=True, max_digits=10)),
                ('vrednost_opis', models.CharField(verbose_name='vrednost-opisno', max_length=255, null=True, blank=True)),
                ('ponudba', models.ForeignKey(to='povprasevanje.Ponudba')),
            ],
            options={
                'verbose_name_plural': 'ponudbe po postavkah',
            },
        ),
        migrations.CreateModel(
            name='Postavka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
                ('datum', models.DateField(verbose_name='datum')),
                ('priloge', models.ManyToManyField(verbose_name='priloge', to='arhiv.Arhiviranje', blank=True, related_name='povprasevanje_priloge')),
                ('zahtevek', models.ForeignKey(null=True, blank=True, verbose_name='zahtevek', to='zahtevki.Zahtevek')),
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
            field=models.ManyToManyField(verbose_name='priloge', to='arhiv.Arhiviranje', blank=True, related_name='postavka_priloge'),
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
            field=models.ForeignKey(null=True, blank=True, verbose_name='referenca - dokumentacija', to='arhiv.Arhiviranje', related_name='referenca_dokument'),
        ),
        migrations.AddField(
            model_name='ponudba',
            name='vrednost_postavke',
            field=models.ManyToManyField(verbose_name='vrednost postavke', through='povprasevanje.PonudbaPoPostavki', to='povprasevanje.Postavka', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='ponudbapopostavki',
            unique_together=set([('postavka', 'ponudba')]),
        ),
    ]
