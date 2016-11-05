# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0004_auto_20160105_1048'),
        ('zahtevki', '0008_auto_20161101_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlinejaSestanka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('vsebina', models.TextField(verbose_name='vsebina alineje')),
                ('predlagal', models.ManyToManyField(verbose_name='predlagal', related_name='predlagal', to='partnerji.Oseba')),
                ('proti_predlogu', models.ManyToManyField(verbose_name='proti predlogu', related_name='proti_predlogu', to='partnerji.Oseba')),
            ],
            options={
                'verbose_name': 'alineja sestanka',
                'verbose_name_plural': 'alineje sestanka',
            },
        ),
        migrations.CreateModel(
            name='Sestanek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('datum', models.DateField(verbose_name='datum sestanka', blank=True, null=True)),
                ('sklicatelj', models.ForeignKey(blank=True, null=True, to='partnerji.SkupinaPartnerjev')),
                ('udelezenci', models.ManyToManyField(verbose_name='udeleženci', blank=True, to='partnerji.Oseba')),
                ('zahtevek', models.OneToOneField(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='TemaSestankov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('predlagal', models.CharField(max_length=255)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'tema sestankovanja',
                'verbose_name_plural': 'teme sestankovanja',
            },
        ),
        migrations.CreateModel(
            name='TockaSestanka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('naziv_tocke', models.CharField(max_length=255)),
                ('predlagal', models.ForeignKey(verbose_name='predlagal', to='partnerji.Oseba')),
                ('tema_sestanka', models.ForeignKey(verbose_name='tema sestanka', to='sestanki.TemaSestankov')),
            ],
            options={
                'verbose_name': 'točka sestanka',
                'verbose_name_plural': 'točke sestanka',
            },
        ),
        migrations.AddField(
            model_name='alinejasestanka',
            name='tocka_sestanka',
            field=models.ForeignKey(verbose_name='točka', to='sestanki.TockaSestanka'),
        ),
    ]
