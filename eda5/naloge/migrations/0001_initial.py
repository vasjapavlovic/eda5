# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Naloga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('prioriteta', models.IntegerField(default=1, choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(verbose_name='naziv naloge', max_length=255)),
                ('opis', models.TextField(verbose_name='opis naloge', null=True, blank=True)),
                ('rok_izvedbe', models.DateField(verbose_name='rok za izvedbo')),
            ],
            options={
                'verbose_name': 'naloga',
                'verbose_name_plural': 'naloge',
            },
        ),
    ]
