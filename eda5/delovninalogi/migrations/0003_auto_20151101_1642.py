# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0002_opravilo_vrsta_stroska'),
    ]

    operations = [
        migrations.AddField(
            model_name='delo',
            name='status',
            field=models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0),
        ),
        migrations.AddField(
            model_name='delovninalog',
            name='status',
            field=models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0),
        ),
        migrations.AddField(
            model_name='opravilo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
