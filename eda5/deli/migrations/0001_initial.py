# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.deli.models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelStavbe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('shema', models.FileField(upload_to=eda5.deli.models.DelStavbe.shema_directory_path, blank=True, verbose_name='shema sistema')),
            ],
            options={
                'verbose_name': 'del stavbe',
                'verbose_name_plural': 'deli stavbe',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, verbose_name='Oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='Naziv')),
                ('serijska_st', models.CharField(max_length=100, blank=True, verbose_name='Serijska Številka')),
                ('tovarniska_st', models.CharField(max_length=100, blank=True, verbose_name='Tovarniška Številka')),
                ('datum_prevzema_v_upravljanje', models.DateField(verbose_name='datum prevzema v upravljanje', blank=True)),
                ('dokumentacija', models.FileField(upload_to=eda5.deli.models.Element.dokumentacija_directory_path, blank=True, verbose_name='dokumentacija')),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe')),
                ('model_artikla', models.ForeignKey(default=1, verbose_name='Model', to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name': 'element',
                'verbose_name_plural': 'elementi',
            },
        ),
        migrations.CreateModel(
            name='Podskupina',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'podskupina delov',
                'verbose_name_plural': 'podskupine delov',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Skupina',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'skupina delov',
                'verbose_name_plural': 'skupine delov',
                'ordering': ['oznaka'],
            },
        ),
        migrations.AddField(
            model_name='podskupina',
            name='skupina',
            field=models.ForeignKey(to='deli.Skupina'),
        ),
    ]
