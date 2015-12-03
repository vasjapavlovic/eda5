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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=4)),
                ('status', models.IntegerField(choices=[(1, 'v uporabi'), (2, 'izklopljen')], default=1)),
                ('stevilka', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'verbose_name': 'daljinec',
                'verbose_name_plural': 'daljinci',
            },
        ),
        migrations.CreateModel(
            name='PredajaDaljinca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=4)),
                ('datum', models.DateField()),
                ('daljinec', models.ForeignKey(to='predaja_lastnine.Daljinec')),
            ],
            options={
                'verbose_name': 'predaja daljinca',
                'verbose_name_plural': 'predaje daljincev',
            },
        ),
        migrations.CreateModel(
            name='PredajaLastnine',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=4)),
                ('datum', models.DateField()),
                ('tip_predaje', models.CharField(verbose_name='tip predaje etažne lastnine', choices=[('P', 'predaja v last'), ('N', 'predaja v najem')], max_length=1)),
                ('trajanje', models.CharField(max_length=50, blank=True)),
                ('dokument', models.CharField(max_length=50, blank=True)),
                ('daljinec', models.ManyToManyField(through='predaja_lastnine.PredajaDaljinca', to='predaja_lastnine.Daljinec')),
                ('kupec', models.ForeignKey(to='partnerji.Partner', related_name='kupec')),
                ('lastniska_enota_interna', models.ForeignKey(to='etaznalastnina.LastniskaEnotaInterna', verbose_name='Interna lastniška enota')),
                ('prodajalec', models.ForeignKey(to='partnerji.Partner', related_name='prodajalec')),
            ],
            options={
                'verbose_name': 'predaja lastnine',
                'verbose_name_plural': 'predaje lastnine',
            },
        ),
        migrations.AddField(
            model_name='predajadaljinca',
            name='predaja_lastnine',
            field=models.ForeignKey(to='predaja_lastnine.PredajaLastnine'),
        ),
    ]
