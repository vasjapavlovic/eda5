# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '__first__'),
        ('arhiv', '0003_arhiviranje_razdelilnik'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='dogodek',
            field=models.ForeignKey(null=True, to='dogodki.Dogodek', blank=True),
        ),
    ]
