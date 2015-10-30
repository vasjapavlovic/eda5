# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0005_auto_20151029_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastniskaSkupina',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'verbose_name_plural': 'lastniške skupine',
                'ordering': ('oznaka',),
                'verbose_name': 'lastniška skupina',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
            ],
            options={
                'verbose_name_plural': 'Programi',
                'ordering': ('zap_st',),
                'verbose_name': 'Program',
            },
        ),
        migrations.AddField(
            model_name='lastniskaskupina',
            name='program',
            field=models.ForeignKey(to='etaznalastnina.Program'),
        ),
    ]
