# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_skupinapartnerjev_oznaka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arhiv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('elektronski', models.BooleanField(verbose_name='elektronski hramba', default=True)),
                ('fizicni', models.BooleanField(verbose_name='fizični hramba', default=False)),
                ('arhiviral', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'verbose_name': 'arhiviranje',
                'verbose_name_plural': 'arhiviranje',
            },
        ),
        migrations.CreateModel(
            name='ArhivMesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=10)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('arhiv', models.ForeignKey(to='arhiv.Arhiv')),
            ],
            options={
                'verbose_name': 'arhivsko mesto',
                'verbose_name_plural': 'arhivska mesta',
            },
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='lokacija_hrambe',
            field=models.ForeignKey(to='arhiv.ArhivMesto', null=True, verbose_name='lokacija hrambe', blank=True),
        ),
    ]
