# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0012_auto_20180106_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='vzorecopravila',
            name='opis',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vzorecopravila',
            name='oznaka_gen',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vzorecopravila',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')]),
        ),
        migrations.AlterField(
            model_name='vzorecopravila',
            name='is_potrjen',
            field=models.BooleanField(verbose_name='Potrjeno s strani nadzornika', default=False),
        ),
        migrations.AlterField(
            model_name='vzorecopravila',
            name='naziv',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vzorecopravila',
            name='oznaka',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
