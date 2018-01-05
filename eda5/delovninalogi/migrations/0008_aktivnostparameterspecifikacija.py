# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0007_aktivnost_projektno_mesto'),
    ]

    operations = [
        migrations.CreateModel(
            name='AktivnostParameterSpecifikacija',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(null=True, blank=True, max_length=100)),
                ('oznaka_gen', models.CharField(null=True, blank=True, max_length=100)),
                ('naziv', models.CharField(null=True, blank=True, max_length=255)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('aktivnost', models.ForeignKey(verbose_name='aktivnost', to='delovninalogi.Aktivnost')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
