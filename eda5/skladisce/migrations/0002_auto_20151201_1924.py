# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skladisce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='dnevnik',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dnevnik',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='dobava',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dobava',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
