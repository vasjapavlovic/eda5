# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obvestila', '0005_obvestilo_objavljeno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Povezava',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('url_ref', models.CharField(max_length=500, blank=True)),
                ('naziv', models.CharField(max_length=255)),
                ('predtext', models.CharField(max_length=255)),
                ('objavljeno', models.BooleanField(default=False)),
                ('obvestilo', models.ForeignKey(to='obvestila.Obvestilo')),
            ],
            options={
                'verbose_name': 'povezava',
                'verbose_name_plural': 'povezave',
            },
        ),
    ]
