# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0002_auto_20151203_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='KarakteristikaVrednost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('vrednost', models.CharField(max_length=20)),
                ('artikel', models.ForeignKey(blank=True, null=True, to='katalog.ModelArtikla')),
                ('karakteristika', models.ForeignKey(to='katalog.Karakteristika')),
            ],
            options={
                'verbose_name': 'vrednost karakteristike',
                'verbose_name_plural': 'vrednosti karakteristik',
            },
        ),
    ]
