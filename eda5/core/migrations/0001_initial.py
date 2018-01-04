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
                ('oznaka', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ('-oznaka',),
            },
        ),
        migrations.CreateModel(
            name='ObdobjeMesec',
            fields=[
                ('oznaka', models.IntegerField(serialize=False, primary_key=True)),
                ('naziv', models.CharField(max_length=10)),
            ],
        ),
    ]
