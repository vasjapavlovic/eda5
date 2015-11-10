# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('lastnistvo', '0001_initial'),
        ('racunovodstvo', '0002_racun_is_likvidiran'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SkupinaStroska',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Strosek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('lastniska_skupina', models.ForeignKey(to='lastnistvo.LastniskaSkupina')),
                ('racun', models.ForeignKey(to='racunovodstvo.Racun')),
            ],
            options={
                'verbose_name': 'strošek',
                'verbose_name_plural': 'stroški',
            },
        ),
        migrations.CreateModel(
            name='VrstaStroska',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
    ]
