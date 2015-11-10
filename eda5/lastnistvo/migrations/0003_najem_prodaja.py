# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0013_auto_20151030_1310'),
        ('etaznalastnina', '0009_auto_20151110_0117'),
        ('posta', '0008_auto_20151026_0727'),
        ('lastnistvo', '0002_auto_20151110_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Najem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v najem')),
                ('trajanje_enota', models.CharField(verbose_name='enota trajanja najema', max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')])),
                ('trajanje_kolicina', models.IntegerField(verbose_name='količina trajanja/enota')),
                ('placnik_stroskov', models.CharField(verbose_name='plačnik stroškov', max_length=8, choices=[(1, 'lastnik'), (2, 'najemnik')])),
                ('lastniska_enota', models.ManyToManyField(verbose_name='lastniška enota', to='etaznalastnina.LastniskaEnotaInterna')),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v posest')),
                ('datum_vpisa', models.DateField(verbose_name='datum vpisa v zemljiško knjigo', null=True, blank=True)),
                ('kupec', models.ForeignKey(to='partnerji.SkupinaPartnerjev')),
                ('lastniska_enota', models.ManyToManyField(verbose_name='lastniška enota', to='etaznalastnina.LastniskaEnotaElaborat')),
                ('zapisnik_predaje', models.ForeignKey(verbose_name='zapisnik predaje v posest', to='posta.Dokument')),
            ],
            options={
                'verbose_name': 'prodaja',
                'verbose_name_plural': 'prodaja',
            },
        ),
    ]
