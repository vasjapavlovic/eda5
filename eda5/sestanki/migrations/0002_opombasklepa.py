# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpombaSklepa',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')])),
                ('oznaka', models.CharField(max_length=255, verbose_name='oznaka')),
                ('opis', models.TextField(verbose_name='vsebina')),
                ('opomnil', models.CharField(null=True, max_length=255, blank=True, verbose_name='opomnil')),
                ('sklep', models.ForeignKey(verbose_name='sklep sestanka', to='sestanki.Tocka')),
            ],
            options={
                'verbose_name_plural': 'opombe sklepov',
                'verbose_name': 'opomba sklepa',
            },
        ),
    ]
