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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
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
