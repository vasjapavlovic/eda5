# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etaza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=50, unique=True)),
                ('naziv', models.CharField(verbose_name='Naziv', max_length=255, null=True, blank=True)),
                ('opis', models.TextField(verbose_name='Opis', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Etaža',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'Etaže',
            },
        ),
        migrations.CreateModel(
            name='Prostor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=20, unique=True)),
                ('naziv', models.CharField(verbose_name='Naziv', max_length=255, null=True, blank=True)),
                ('opis', models.TextField(verbose_name='Opis', null=True, blank=True)),
                ('bim_id', models.CharField(verbose_name='BIM ID', max_length=100, null=True, blank=True)),
                ('etaza', models.ForeignKey(verbose_name='Etaža', to='lokacija.Etaza')),
            ],
            options={
                'verbose_name': 'Prostor',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'Prostori',
            },
        ),
        migrations.CreateModel(
            name='Stavba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=20, unique=True)),
                ('naziv', models.CharField(verbose_name='Naziv', max_length=255, null=True, blank=True)),
                ('opis', models.TextField(verbose_name='Opis', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Stavba',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'Stavbe',
            },
        ),
        migrations.AddField(
            model_name='etaza',
            name='stavba',
            field=models.ForeignKey(verbose_name='Stavba', to='lokacija.Stavba'),
        ),
    ]
