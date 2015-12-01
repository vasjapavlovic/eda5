# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0004_planizdaja_oznaka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='planizdaja',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='planizdaja',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='planopravilo',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='planopravilo',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
