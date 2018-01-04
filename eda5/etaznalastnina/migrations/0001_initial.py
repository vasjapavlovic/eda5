# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InternaDodatno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('stanje_prostora', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'dodatek interni LE',
                'ordering': ['interna'],
                'verbose_name_plural': 'dodatki internim LE',
            },
        ),
        migrations.CreateModel(
            name='LastniskaEnotaElaborat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(verbose_name='številka dela stavbe', max_length=4, unique=True)),
                ('opis', models.CharField(max_length=255, blank=True)),
                ('naslov', models.CharField(max_length=255)),
                ('povrsina_tlorisna_neto', models.DecimalField(verbose_name='neto tlorisna površina', decimal_places=2, max_digits=6)),
                ('lastniski_delez', models.DecimalField(verbose_name='lastniški delež', decimal_places=4, null=True, blank=True, max_digits=5)),
            ],
            options={
                'verbose_name': 'lastniška enota elaborat',
                'ordering': ('id',),
                'verbose_name_plural': 'lastniške enote elaborat',
            },
        ),
        migrations.CreateModel(
            name='LastniskaEnotaInterna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(verbose_name='interna številka dela stavbe', max_length=5, unique=True)),
                ('lastniski_delez', models.DecimalField(verbose_name='lastniški delež', decimal_places=4, blank=True, max_digits=5)),
                ('povrsina_tlorisna_neto', models.DecimalField(verbose_name='neto tlorisna površina', decimal_places=2, max_digits=6)),
                ('st_oseb', models.DecimalField(verbose_name='število oseb', decimal_places=1, blank=True, max_digits=2)),
                ('elaborat', models.ForeignKey(verbose_name='Relacija na Elaborat Etažne Lastnine', to='etaznalastnina.LastniskaEnotaElaborat')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
            ],
            options={
                'verbose_name': 'Program',
                'ordering': ('zap_st',),
                'verbose_name_plural': 'Programi',
            },
        ),
        migrations.CreateModel(
            name='UporabnoDovoljenje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('st_dokumenta', models.CharField(max_length=50, unique=True)),
                ('datum', models.DateField()),
                ('objekt', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'uporabno dovoljenje',
                'ordering': ['datum'],
                'verbose_name_plural': 'uporabna dovoljenja',
            },
        ),
        migrations.AddField(
            model_name='lastniskaskupina',
            name='program',
            field=models.ForeignKey(to='etaznalastnina.Program'),
        ),
    ]
