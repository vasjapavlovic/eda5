# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0010_opcijeselect'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpcijaSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('oznaka', models.CharField(null=True, max_length=100, blank=True)),
                ('oznaka_gen', models.CharField(null=True, max_length=100, blank=True)),
                ('naziv', models.CharField(null=True, max_length=255, blank=True)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')], default=0)),
                ('aktivnost_parameter_specifikacija', models.ForeignKey(to='delovninalogi.AktivnostParameterSpecifikacija', verbose_name='aktivnost parameter specifikacija')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='opcijeselect',
            name='aktivnost_parameter_specifikacija',
        ),
        migrations.DeleteModel(
            name='OpcijeSelect',
        ),
    ]
