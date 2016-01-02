# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0010_remove_predajalastnine_vrsta_predaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='najemlastnine',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
