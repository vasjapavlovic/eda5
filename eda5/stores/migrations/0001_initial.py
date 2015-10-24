# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IceCreamStore',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('block_address', models.TextField()),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('description', models.TextField(help_text='Enter a destription of the store', blank=True)),
            ],
        ),
    ]
