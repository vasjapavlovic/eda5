# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelartikla',
            name='created',
        ),
        migrations.RemoveField(
            model_name='modelartikla',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='planov',
            name='created',
        ),
        migrations.RemoveField(
            model_name='planov',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='proizvajalec',
            name='created',
        ),
        migrations.RemoveField(
            model_name='proizvajalec',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='rezervnidel',
            name='created',
        ),
        migrations.RemoveField(
            model_name='rezervnidel',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='tipartikla',
            name='created',
        ),
        migrations.RemoveField(
            model_name='tipartikla',
            name='updated',
        ),
    ]
