# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0003_auto_20151219_0936'),
        ('etaznalastnina', '0015_auto_20151219_0936'),
        ('lastnistvo', '0002_auto_20151215_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredajaLastnine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('vrsta_predaje', models.IntegerField(choices=[(1, 'predaja v last'), (2, 'predaja v najem')])),
                ('datum_predaje', models.DateField()),
                ('datum_veljavnosti', models.DateField(null=True, blank=True)),
                ('placnik_stroskov', models.IntegerField(verbose_name='plačnik stroškov', null=True, blank=True, choices=[(1, 'lastnik'), (2, 'najemnik')])),
                ('kupec', models.ForeignKey(related_name='kupec', to='partnerji.SkupinaPartnerjev')),
                ('lastniska_enota', models.ManyToManyField(verbose_name='lastniška enota', to='etaznalastnina.LastniskaEnotaElaborat')),
                ('prodajalec', models.ForeignKey(related_name='prodajalec', to='partnerji.SkupinaPartnerjev')),
            ],
            options={
                'verbose_name': 'predaja lastnine',
                'verbose_name_plural': 'predaje lastnine',
            },
        ),
        migrations.RemoveField(
            model_name='najem',
            name='lastniska_enota',
        ),
        migrations.RemoveField(
            model_name='najem',
            name='najemna_pogodba',
        ),
        migrations.RemoveField(
            model_name='najem',
            name='najemnik',
        ),
        migrations.RemoveField(
            model_name='prodaja',
            name='kupec',
        ),
        migrations.RemoveField(
            model_name='prodaja',
            name='lastniska_enota',
        ),
        migrations.RemoveField(
            model_name='prodaja',
            name='zapisnik_predaje',
        ),
        migrations.DeleteModel(
            name='Najem',
        ),
        migrations.DeleteModel(
            name='Prodaja',
        ),
    ]
