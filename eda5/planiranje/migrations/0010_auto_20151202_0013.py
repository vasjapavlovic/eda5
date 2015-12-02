# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0006_auto_20151202_0013'),
        ('planiranje', '0009_auto_20151202_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaniranaAktivnost',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'planirane aktivnosti',
                'verbose_name': 'planirana aktivnost',
            },
        ),
        migrations.CreateModel(
            name='PlaniranoOpravilo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('namen', models.CharField(max_length=255)),
                ('obseg', models.TextField()),
                ('perioda_predpisana_enota', models.CharField(max_length=5, verbose_name='enota periode', choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')])),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('opomba', models.TextField(blank=True)),
                ('plan', models.ForeignKey(to='planiranje.Plan')),
            ],
            options={
                'verbose_name_plural': 'planirana opravila',
                'verbose_name': 'planirano opravilo',
            },
        ),
        migrations.RemoveField(
            model_name='planopravilo',
            name='plan',
        ),
        migrations.DeleteModel(
            name='PlanOpravilo',
        ),
    ]
