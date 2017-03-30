# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0013_naloga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naloga',
            name='datum',
        ),
        migrations.AddField(
            model_name='naloga',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='naloga',
            name='is_likvidiran',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='naloga',
            name='prioriteta',
            field=models.IntegerField(default=1, choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')]),
        ),
        migrations.AddField(
            model_name='naloga',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')]),
        ),
        migrations.AddField(
            model_name='naloga',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='naloga',
            name='naziv',
            field=models.CharField(max_length=255, verbose_name='naziv naloge'),
        ),
        migrations.AlterField(
            model_name='naloga',
            name='opis',
            field=models.TextField(null=True, verbose_name='opis naloge', blank=True),
        ),
    ]
