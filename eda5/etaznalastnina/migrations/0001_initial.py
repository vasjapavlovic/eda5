# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastniskaEnotaElaborat',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=4, verbose_name='številka dela stavbe')),
                ('povrsina_tlorisna_neto', models.CharField(max_length=4, verbose_name='neto tlorisna površina')),
                ('naslov', models.CharField(max_length=255)),
                ('posta', models.ForeignKey(verbose_name='pošta', to='partnerji.Posta')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=5, verbose_name='interna številka dela stavbe')),
                ('lastniski_delez', models.DecimalField(decimal_places=4, verbose_name='lastniški delež', blank=True, max_digits=5)),
                ('povrsina_tlorisna_neto', models.CharField(max_length=4, verbose_name='neto tlorisna površina', blank=True)),
                ('st_oseb', models.IntegerField(verbose_name='število oseb', blank=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
