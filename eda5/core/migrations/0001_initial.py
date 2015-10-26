# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObdobjeLeto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(max_length=4)),
                ('naziv', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ObdobjeMesec',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(max_length=2)),
                ('naziv', models.CharField(max_length=10)),
            ],
        ),
    ]
