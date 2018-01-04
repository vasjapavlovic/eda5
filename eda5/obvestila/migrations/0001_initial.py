# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('vsebina', models.TextField()),
            ],
            options={
                'verbose_name': 'komentar',
                'ordering': ['-created'],
                'verbose_name_plural': 'komentarji',
            },
        ),
        migrations.CreateModel(
            name='Obvestilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('vsebina', models.TextField()),
            ],
            options={
                'verbose_name': 'obvestilo',
                'ordering': ['-created'],
                'verbose_name_plural': 'obvestila',
            },
        ),
        migrations.CreateModel(
            name='Povezava',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('url_ref', models.CharField(max_length=500)),
                ('naziv', models.CharField(max_length=255)),
                ('predtext', models.CharField(max_length=255, blank=True)),
                ('objavljeno', models.BooleanField(default=False)),
                ('url_detail', models.CharField(max_length=50, blank=True)),
                ('obvestilo', models.ForeignKey(to='obvestila.Obvestilo')),
            ],
            options={
                'verbose_name': 'povezava',
                'verbose_name_plural': 'povezave',
            },
        ),
    ]
