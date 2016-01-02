# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0016_auto_20160101_2333'),
        ('partnerji', '0003_auto_20151219_0936'),
        ('lastnistvo', '0006_auto_20160101_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='NajemLastnine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('datum_predaje', models.DateField()),
                ('datum_veljavnosti', models.DateField(blank=True, null=True)),
                ('lastniska_enota', models.ForeignKey(to='etaznalastnina.LastniskaEnotaInterna', related_name='le_interna', verbose_name='LE', blank=True, null=True)),
                ('placnik', models.ForeignKey(related_name='placnik', to='partnerji.SkupinaPartnerjev')),
            ],
            options={
                'verbose_name_plural': 'najem lastnine',
                'verbose_name': 'najem lastnine',
            },
        ),
        migrations.CreateModel(
            name='ProdajaLastnine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('datum_predaje', models.DateField()),
                ('lastniska_enota', models.ForeignKey(to='etaznalastnina.LastniskaEnotaElaborat', verbose_name='LE', blank=True, null=True)),
                ('placnik', models.ForeignKey(related_name='plačnik', to='partnerji.SkupinaPartnerjev')),
            ],
            options={
                'verbose_name_plural': 'prodaja lastnine',
                'verbose_name': 'prodaja lastnine',
            },
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='datum_predaje',
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='datum_veljavnosti',
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='lastniska_enota_elaborat',
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='lastniska_enota_interna',
        ),
        migrations.RemoveField(
            model_name='predajalastnine',
            name='placnik_stroskov',
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='predaja_lastnine',
            field=models.ForeignKey(to='lastnistvo.PredajaLastnine'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='predaja_lastnine',
            field=models.ForeignKey(to='lastnistvo.PredajaLastnine'),
        ),
    ]
