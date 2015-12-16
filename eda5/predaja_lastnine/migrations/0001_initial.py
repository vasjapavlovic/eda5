# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daljinec',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=4)),
                ('status', models.IntegerField(choices=[(1, 'v uporabi'), (2, 'izklopljen')], default=1)),
                ('stevilka', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'daljinci',
                'verbose_name': 'daljinec',
            },
        ),
        migrations.CreateModel(
            name='PredajaDaljinca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=4)),
                ('datum', models.DateField()),
                ('daljinec', models.ForeignKey(to='predaja_lastnine.Daljinec')),
            ],
            options={
                'verbose_name_plural': 'predaje daljincev',
                'verbose_name': 'predaja daljinca',
            },
        ),
        migrations.CreateModel(
            name='PredajaLastnine',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=4)),
                ('datum', models.DateField()),
                ('tip_predaje', models.CharField(choices=[('P', 'predaja v last'), ('N', 'predaja v najem')], max_length=1, verbose_name='tip predaje etažne lastnine')),
                ('trajanje', models.CharField(blank=True, max_length=50)),
                ('dokument', models.CharField(blank=True, max_length=50)),
                ('daljinec', models.ManyToManyField(through='predaja_lastnine.PredajaDaljinca', to='predaja_lastnine.Daljinec')),
                ('kupec', models.ForeignKey(to='partnerji.Partner', related_name='kupec')),
                ('lastniska_enota_interna', models.ForeignKey(to='etaznalastnina.LastniskaEnotaInterna', verbose_name='Interna lastniška enota')),
                ('prodajalec', models.ForeignKey(to='partnerji.Partner', related_name='prodajalec')),
            ],
            options={
                'verbose_name_plural': 'predaje lastnine',
                'verbose_name': 'predaja lastnine',
            },
        ),
        migrations.AddField(
            model_name='predajadaljinca',
            name='predaja_lastnine',
            field=models.ForeignKey(to='predaja_lastnine.PredajaLastnine'),
        ),
    ]
