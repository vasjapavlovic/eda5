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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=50, unique=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True, verbose_name='Naziv')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='Opis')),
            ],
            options={
                'verbose_name_plural': 'Etaže',
                'verbose_name': 'Etaža',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Prostor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=20, unique=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True, verbose_name='Naziv')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('bim_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='BIM ID')),
                ('etaza', models.ForeignKey(verbose_name='Etaža', to='lokacija.Etaza')),
            ],
            options={
                'verbose_name_plural': 'Prostori',
                'verbose_name': 'Prostor',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Stavba',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=20, unique=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True, verbose_name='Naziv')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='Opis')),
            ],
            options={
                'verbose_name_plural': 'Stavbe',
                'verbose_name': 'Stavba',
                'ordering': ['oznaka'],
            },
        ),
        migrations.AddField(
            model_name='etaza',
            name='stavba',
            field=models.ForeignKey(verbose_name='Stavba', to='lokacija.Stavba'),
        ),
    ]
