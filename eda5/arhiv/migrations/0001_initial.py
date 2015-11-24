# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arhiv',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=10, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
            ],
            options={
                'verbose_name': 'arhiv',
                'verbose_name_plural': 'arhivi',
            },
        ),
        migrations.CreateModel(
            name='Arhiviranje',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('elektronski', models.BooleanField(verbose_name='elektronski hramba', default=True)),
                ('fizicni', models.BooleanField(verbose_name='fizični hramba', default=False)),
            ],
            options={
                'verbose_name': 'arhiviranje',
                'verbose_name_plural': 'arhiviranje',
            },
        ),
        migrations.CreateModel(
            name='ArhivMesto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=10, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('arhiv', models.ForeignKey(to='arhiv.Arhiv')),
            ],
            options={
                'verbose_name': 'arhivsko mesto',
                'verbose_name_plural': 'arhivska mesta',
            },
        ),
    ]
