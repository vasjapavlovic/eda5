# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0015_opravilo_zmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='status',
            field=models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0),
        ),
    ]
