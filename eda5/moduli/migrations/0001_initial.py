# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(max_length=10)),
                ('naziv', models.CharField(max_length=200)),
                ('opis', models.TextField()),
                ('url_name', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
