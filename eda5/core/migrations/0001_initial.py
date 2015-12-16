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
                ('oznaka', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ObdobjeMesec',
            fields=[
                ('oznaka', models.IntegerField(primary_key=True, serialize=False)),
                ('naziv', models.CharField(max_length=10)),
            ],
        ),
    ]
