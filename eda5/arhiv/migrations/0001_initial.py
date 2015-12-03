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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=10)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
            ],
            options={
                'verbose_name': 'arhiv',
                'verbose_name_plural': 'arhivi',
            },
        ),
        migrations.CreateModel(
            name='Arhiviranje',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=10)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('arhiv', models.ForeignKey(to='arhiv.Arhiv')),
            ],
            options={
                'verbose_name': 'arhivsko mesto',
                'verbose_name_plural': 'arhivska mesta',
            },
        ),
    ]
