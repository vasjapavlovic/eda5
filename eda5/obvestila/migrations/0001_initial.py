# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('vsebina', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'komentarji',
                'verbose_name': 'komentar',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Obvestilo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('vsebina', models.TextField()),
                ('oseba', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'verbose_name_plural': 'obvestila',
                'verbose_name': 'obvestilo',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Povezava',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url_ref', models.CharField(max_length=500)),
                ('naziv', models.CharField(max_length=255)),
                ('predtext', models.CharField(blank=True, max_length=255)),
                ('objavljeno', models.BooleanField(default=False)),
                ('url_detail', models.CharField(blank=True, max_length=50)),
                ('obvestilo', models.ForeignKey(to='obvestila.Obvestilo')),
            ],
            options={
                'verbose_name_plural': 'povezave',
                'verbose_name': 'povezava',
            },
        ),
        migrations.AddField(
            model_name='komentar',
            name='obvestilo',
            field=models.ForeignKey(to='obvestila.Obvestilo'),
        ),
    ]
