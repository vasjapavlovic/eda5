# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NadzornaEnota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('ip_naslov', models.CharField(max_length=255)),
                ('opis', models.TextField()),
            ],
            options={
                'verbose_name': 'nadzorna enota',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'nadzorne enote',
            },
        ),
        migrations.CreateModel(
            name='NadzorniSistem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'nadzorni sistem',
                'verbose_name_plural': 'nadzorni sistemi',
            },
        ),
        migrations.AddField(
            model_name='nadzornaenota',
            name='nadzorni_sistem',
            field=models.ForeignKey(to='nadzornaplosca.NadzorniSistem'),
        ),
    ]
