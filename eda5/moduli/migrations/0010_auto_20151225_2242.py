# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0009_auto_20151225_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zavihek',
            name='parent',
        ),
        migrations.AddField(
            model_name='zavihek',
            name='parent',
            field=models.ManyToManyField(related_name='_parent_+', blank=True, to='moduli.Zavihek'),
        ),
    ]
