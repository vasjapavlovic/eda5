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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=4, verbose_name='številka dela stavbe')),
                ('povrsina_tlorisna_neto', models.DecimalField(max_digits=6, decimal_places=2, verbose_name='neto tlorisna površina')),
                ('naslov', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'lastniške enote elaborat',
                'verbose_name': 'lastniška enota elaborat',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='LastniskaEnotaInterna',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=5, verbose_name='interna številka dela stavbe')),
                ('program', models.CharField(max_length=50)),
                ('lastniski_delez', models.DecimalField(max_digits=5, blank=True, decimal_places=4, verbose_name='lastniški delež')),
                ('povrsina_tlorisna_neto', models.DecimalField(max_digits=6, decimal_places=2, verbose_name='neto tlorisna površina')),
                ('st_oseb', models.DecimalField(max_digits=2, blank=True, decimal_places=1, verbose_name='število oseb')),
                ('elaborat', models.ForeignKey(to='etaznalastnina.LastniskaEnotaElaborat')),
            ],
            options={
                'verbose_name_plural': 'lastniške enote interna',
                'verbose_name': 'lastniška enota interna',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='LastniskaSkupina',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(blank=True, max_length=255)),
                ('lastniska_enota', models.ManyToManyField(blank=True, to='etaznalastnina.LastniskaEnotaElaborat')),
            ],
            options={
                'verbose_name_plural': 'lastniške skupine',
                'verbose_name': 'lastniška skupina',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
            ],
            options={
                'verbose_name_plural': 'Programi',
                'verbose_name': 'Program',
                'ordering': ('zap_st',),
            },
        ),
        migrations.AddField(
            model_name='lastniskaskupina',
            name='program',
            field=models.ForeignKey(to='etaznalastnina.Program'),
        ),
    ]
