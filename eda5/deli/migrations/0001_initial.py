# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.deli.models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0001_initial'),
        ('katalog', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelStavbe',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('shema', models.FileField(verbose_name='shema sistema', blank=True, upload_to=eda5.deli.models.DelStavbe.shema_directory_path)),
                ('lastniska_skupina', models.ForeignKey(to='etaznalastnina.LastniskaSkupina', verbose_name='lastniška skupina', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'del stavbe',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'deli stavbe',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20, verbose_name='Oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='Naziv')),
                ('serijska_st', models.CharField(max_length=100, verbose_name='Serijska Številka', blank=True)),
                ('tovarniska_st', models.CharField(max_length=100, verbose_name='Tovarniška Številka', blank=True)),
                ('datum_prevzema_v_upravljanje', models.DateField(verbose_name='datum prevzema v upravljanje', blank=True)),
                ('dokumentacija', models.FileField(verbose_name='dokumentacija', blank=True, upload_to=eda5.deli.models.Element.dokumentacija_directory_path)),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe')),
                ('model_artikla', models.ForeignKey(to='katalog.ModelArtikla', verbose_name='Model', default=1)),
                ('prejeta_dokumentacija', models.ManyToManyField(to='posta.Dokument', blank=True)),
            ],
            options={
                'verbose_name': 'element',
                'verbose_name_plural': 'elementi',
            },
        ),
        migrations.CreateModel(
            name='Podskupina',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'podskupina delov',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'podskupine delov',
            },
        ),
        migrations.CreateModel(
            name='Skupina',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'skupina delov',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'skupine delov',
            },
        ),
        migrations.AddField(
            model_name='podskupina',
            name='skupina',
            field=models.ForeignKey(to='deli.Skupina'),
        ),
        migrations.AddField(
            model_name='delstavbe',
            name='podskupina',
            field=models.ForeignKey(to='deli.Podskupina'),
        ),
        migrations.AddField(
            model_name='delstavbe',
            name='prejeta_dokumentacija',
            field=models.ManyToManyField(to='posta.Dokument', blank=True),
        ),
    ]
