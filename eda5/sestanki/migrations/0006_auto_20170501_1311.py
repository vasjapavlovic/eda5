# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0005_auto_20170501_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
            ],
            options={
                'verbose_name_plural': 'teme',
                'verbose_name': 'tema',
            },
        ),
        migrations.AlterModelOptions(
            name='vnos',
            options={'verbose_name_plural': 'vnosi sestankov', 'verbose_name': 'vnos sestanka'},
        ),
        migrations.AddField(
            model_name='zadeva',
            name='tema',
            field=models.ForeignKey(null=True, verbose_name='tema', blank=True, to='sestanki.Tema'),
        ),
    ]
