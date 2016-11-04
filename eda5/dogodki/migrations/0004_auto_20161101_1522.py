# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0003_dogodek_cas_dogodka'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='status',
            field=models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'preklicano')], default=0),
        ),
        migrations.AddField(
            model_name='dogodek',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
