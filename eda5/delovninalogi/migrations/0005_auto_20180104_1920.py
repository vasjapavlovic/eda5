# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0004_aktivnost'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktivnost',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='naziv',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='opis',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='oznaka',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='oznaka_gen',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')]),
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
