# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Del',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('shema', models.FileField(verbose_name='shema sistema', blank=True, upload_to='shema_directory_path')),
            ],
            options={
                'verbose_name_plural': 'deli stavbe',
                'ordering': ['oznaka'],
                'verbose_name': 'del stavbe',
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
            ],
            options={
                'verbose_name_plural': 'elementi',
                'verbose_name': 'element',
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
                'verbose_name_plural': 'podskupine delov',
                'ordering': ['oznaka'],
                'verbose_name': 'podskupina delov',
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
                'verbose_name_plural': 'skupine delov',
                'ordering': ['oznaka'],
                'verbose_name': 'skupina delov',
            },
        ),
        migrations.AddField(
            model_name='podskupina',
            name='skupina',
            field=models.ForeignKey(to='deli.Skupina'),
        ),
    ]
