# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0009_auto_20170227_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etaza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', unique=True, max_length=50)),
                ('naziv', models.CharField(verbose_name='Naziv', blank=True, null=True, max_length=255)),
                ('opis', models.TextField(verbose_name='Opis', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Etaža',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'Etaže',
            },
        ),
        migrations.CreateModel(
            name='RelacijaProstorEtaza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('etaza', models.ForeignKey(verbose_name='Etaža', to='deli.Etaza')),
                ('prostor', models.OneToOneField(verbose_name='Prostor', to='deli.DelStavbe')),
            ],
            options={
                'verbose_name': 'Relacija Prostor/Etaža',
                'ordering': ['prostor__oznaka'],
                'verbose_name_plural': 'Relacije Prostor/Etaža',
            },
        ),
        migrations.CreateModel(
            name='Stavba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', unique=True, max_length=20)),
                ('naziv', models.CharField(verbose_name='Naziv', blank=True, null=True, max_length=255)),
                ('opis', models.TextField(verbose_name='Opis', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Stavba',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'Stavbe',
            },
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='lokacija',
            field=models.ForeignKey(verbose_name='Lokacija v Stavbi', blank=True, to='deli.ProjektnoMesto', null=True),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='tip_elementa',
            field=models.ForeignKey(verbose_name='Tip Elementa', blank=True, to='katalog.TipArtikla', null=True),
        ),
        migrations.AddField(
            model_name='etaza',
            name='stavba',
            field=models.ForeignKey(verbose_name='Stavba', to='deli.Stavba'),
        ),
    ]
