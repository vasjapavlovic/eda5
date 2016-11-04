# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0005_auto_20161103_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='is_nastala_skoda',
            field=models.NullBooleanField(verbose_name='Je nastala škoda?'),
        ),
        migrations.AlterField(
            model_name='dogodek',
            name='povzrocitelj',
            field=models.CharField(default='neznan', verbose_name='povzročitelj (opisno)', max_length=255),
        ),
    ]
