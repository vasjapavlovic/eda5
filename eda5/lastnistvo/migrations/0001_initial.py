# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Najem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v najem')),
                ('trajanje_enota', models.CharField(max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], verbose_name='enota trajanja najema')),
                ('trajanje_kolicina', models.IntegerField(verbose_name='količina trajanja/enota')),
                ('placnik_stroskov', models.CharField(max_length=8, choices=[(1, 'lastnik'), (2, 'najemnik')], verbose_name='plačnik stroškov')),
                ('lastniska_enota', models.ManyToManyField(to='etaznalastnina.LastniskaEnotaInterna', verbose_name='lastniška enota')),
                ('najemna_pogodba', models.ForeignKey(verbose_name='najemna pogodba', to='posta.Dokument')),
                ('najemnik', models.ForeignKey(to='partnerji.SkupinaPartnerjev')),
            ],
            options={
                'verbose_name': 'najem',
                'verbose_name_plural': 'najem',
            },
        ),
        migrations.CreateModel(
            name='Prodaja',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v posest')),
                ('datum_vpisa', models.DateField(verbose_name='datum vpisa v zemljiško knjigo', blank=True, null=True)),
                ('kupec', models.ForeignKey(to='partnerji.SkupinaPartnerjev')),
                ('lastniska_enota', models.ManyToManyField(to='etaznalastnina.LastniskaEnotaElaborat', verbose_name='lastniška enota')),
                ('zapisnik_predaje', models.ForeignKey(verbose_name='zapisnik predaje v posest', to='posta.Dokument')),
            ],
            options={
                'verbose_name': 'prodaja',
                'verbose_name_plural': 'prodaja',
            },
        ),
    ]
