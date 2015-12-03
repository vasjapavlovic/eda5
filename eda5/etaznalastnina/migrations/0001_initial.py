# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LastniskaEnotaElaborat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(verbose_name='številka dela stavbe', max_length=4)),
                ('povrsina_tlorisna_neto', models.DecimalField(verbose_name='neto tlorisna površina', max_digits=6, decimal_places=2)),
                ('naslov', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'lastniška enota elaborat',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'lastniške enote elaborat',
            },
        ),
        migrations.CreateModel(
            name='LastniskaEnotaInterna',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(verbose_name='interna številka dela stavbe', max_length=5)),
                ('program', models.CharField(max_length=50)),
                ('lastniski_delez', models.DecimalField(verbose_name='lastniški delež', max_digits=5, decimal_places=4, blank=True)),
                ('povrsina_tlorisna_neto', models.DecimalField(verbose_name='neto tlorisna površina', max_digits=6, decimal_places=2)),
                ('st_oseb', models.DecimalField(verbose_name='število oseb', max_digits=2, decimal_places=1, blank=True)),
                ('elaborat', models.ForeignKey(to='etaznalastnina.LastniskaEnotaElaborat')),
            ],
            options={
                'verbose_name': 'lastniška enota interna',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'lastniške enote interna',
            },
        ),
        migrations.CreateModel(
            name='LastniskaSkupina',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(max_length=255, blank=True)),
                ('lastniska_enota', models.ManyToManyField(to='etaznalastnina.LastniskaEnotaElaborat', blank=True)),
            ],
            options={
                'verbose_name': 'lastniška skupina',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'lastniške skupine',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
            ],
            options={
                'verbose_name': 'Program',
                'ordering': ('zap_st',),
                'verbose_name_plural': 'Programi',
            },
        ),
        migrations.AddField(
            model_name='lastniskaskupina',
            name='program',
            field=models.ForeignKey(to='etaznalastnina.Program'),
        ),
    ]
