# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0016_auto_20170113_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='najemlastnine',
            name='opombe',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prodajalastnine',
            name='opombe',
            field=models.TextField(blank=True, null=True),
        ),
    ]
