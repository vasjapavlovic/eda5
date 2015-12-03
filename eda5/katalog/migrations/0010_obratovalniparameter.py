# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0009_artikelplan_predpis_opravilo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObratovalniParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'obratovalni parametri',
                'verbose_name': 'obratovalni parameter',
            },
        ),
    ]
