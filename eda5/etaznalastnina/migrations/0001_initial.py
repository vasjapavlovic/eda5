# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternaDodatno',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('stanje_prostora', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'dodatki internim LE',
                'verbose_name': 'dodatek interni LE',
                'ordering': ['interna'],
            },
        ),
        migrations.CreateModel(
            name='LastniskaEnotaElaborat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(verbose_name='številka dela stavbe', max_length=4, unique=True)),
                ('opis', models.CharField(blank=True, max_length=255)),
                ('naslov', models.CharField(max_length=255)),
                ('povrsina_tlorisna_neto', models.DecimalField(verbose_name='neto tlorisna površina', max_digits=6, decimal_places=2)),
                ('lastniski_delez', models.DecimalField(blank=True, max_digits=5, decimal_places=4, null=True, verbose_name='lastniški delež')),
                ('posta', models.ForeignKey(verbose_name='pošta', to='partnerji.Posta')),
            ],
            options={
                'verbose_name_plural': 'lastniške enote elaborat',
                'verbose_name': 'lastniška enota elaborat',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='LastniskaEnotaInterna',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(verbose_name='interna številka dela stavbe', max_length=5, unique=True)),
                ('lastniski_delez', models.DecimalField(blank=True, max_digits=5, decimal_places=4, verbose_name='lastniški delež')),
                ('povrsina_tlorisna_neto', models.DecimalField(verbose_name='neto tlorisna površina', max_digits=6, decimal_places=2)),
                ('st_oseb', models.DecimalField(blank=True, max_digits=2, decimal_places=1, verbose_name='število oseb')),
                ('elaborat', models.ForeignKey(verbose_name='Relacija na Elaborat Etažne Lastnine', to='etaznalastnina.LastniskaEnotaElaborat')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
            ],
            options={
                'verbose_name_plural': 'Programi',
                'verbose_name': 'Program',
                'ordering': ('zap_st',),
            },
        ),
        migrations.CreateModel(
            name='UporabnoDovoljenje',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('st_dokumenta', models.CharField(max_length=50, unique=True)),
                ('datum', models.DateField()),
                ('objekt', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'uporabna dovoljenja',
                'verbose_name': 'uporabno dovoljenje',
                'ordering': ['datum'],
            },
        ),
        migrations.AddField(
            model_name='lastniskaskupina',
            name='program',
            field=models.ForeignKey(to='etaznalastnina.Program'),
        ),
        migrations.AddField(
            model_name='lastniskaenotaelaborat',
            name='program',
            field=models.ForeignKey(null=True, blank=True, to='etaznalastnina.Program'),
        ),
        migrations.AddField(
            model_name='internadodatno',
            name='interna',
            field=models.OneToOneField(verbose_name='interna LE', to='etaznalastnina.LastniskaEnotaInterna'),
        ),
        migrations.AddField(
            model_name='internadodatno',
            name='uporabno_dovoljenje',
            field=models.ForeignKey(null=True, blank=True, to='etaznalastnina.UporabnoDovoljenje'),
        ),
    ]
