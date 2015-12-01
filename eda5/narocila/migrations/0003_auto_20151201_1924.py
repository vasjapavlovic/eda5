# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0002_auto_20151122_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narocilo',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='narocilo',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='narocilopogodba',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='narocilopogodba',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='narocilotelefon',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='narocilotelefon',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
