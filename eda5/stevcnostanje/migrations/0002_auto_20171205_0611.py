# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stevcnostanje', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeritevVrsta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('zap_st', models.IntegerField(default=9999, verbose_name='zaporedna številka')),
                ('oznaka', models.CharField(unique=True, max_length=13)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'vrsta meritve',
                'verbose_name_plural': 'vrste meritev',
                'ordering': ('zap_st',),
            },
        ),
        migrations.AddField(
            model_name='delilnik',
            name='naziv',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='delilnik',
            name='meritev_vrsta',
            field=models.ForeignKey(to='stevcnostanje.MeritevVrsta', null=True, blank=True),
        ),
    ]
