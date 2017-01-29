# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0019_auto_20170120_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='najemlastnine',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
