# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0003_arhiviranje_razdelilnik'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeljavnostDokumenta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('velja_od', models.DateField(verbose_name='velja od')),
                ('velja_do', models.DateField(null=True, blank=True, verbose_name='velja do')),
                ('arhiviranje', models.OneToOneField(to='arhiv.Arhiviranje', verbose_name='arhiviranje')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
