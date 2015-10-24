# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecreamstore',
            name='title',
            field=models.CharField(max_length=100, help_text='Title of the store'),
        ),
    ]
