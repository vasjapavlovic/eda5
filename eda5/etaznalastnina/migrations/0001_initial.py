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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=4, verbose_name='številka dela stavbe')),
                ('povrsina_tlorisna_neto', models.CharField(max_length=4, verbose_name='neto tlorisna površina')),
                ('naslov', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'lastniška enota elaborat',
                'verbose_name_plural': 'lastniške enote elaborat',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='LastniskaEnotaInterna',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=5, verbose_name='interna številka dela stavbe')),
                ('lastniski_delez', models.DecimalField(max_digits=5, verbose_name='lastniški delež', blank=True, decimal_places=4)),
                ('povrsina_tlorisna_neto', models.CharField(max_length=4, blank=True, verbose_name='neto tlorisna površina')),
                ('st_oseb', models.IntegerField(verbose_name='število oseb', blank=True)),
                ('elaborat', models.ForeignKey(to='etaznalastnina.LastniskaEnotaElaborat')),
            ],
            options={
                'verbose_name': 'lastniška enota interna',
                'verbose_name_plural': 'lastniške enote interna',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='LastniskaSkupina',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(max_length=255, blank=True)),
                ('lastniska_enota', models.ManyToManyField(to='etaznalastnina.LastniskaEnotaElaborat', blank=True)),
            ],
            options={
                'verbose_name': 'lastniška skupina',
                'verbose_name_plural': 'lastniške skupine',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programi',
                'ordering': ('zap_st',),
            },
        ),
        migrations.AddField(
            model_name='lastniskaskupina',
            name='program',
            field=models.ForeignKey(to='etaznalastnina.Program'),
        ),
    ]
