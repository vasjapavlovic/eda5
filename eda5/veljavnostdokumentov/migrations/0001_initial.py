# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0021_auto_20170129_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeljavnostDokumenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('velja_od', models.DateField(verbose_name='velja od')),
                ('velja_do', models.DateField(verbose_name='velja do')),
                ('dokument', models.OneToOneField(verbose_name='dokument', to='posta.Dokument')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
