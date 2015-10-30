# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0011_auto_20151025_1701'),
        ('users', '0002_auto_20151023_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='partner',
            field=models.ForeignKey(default=2, to='partnerji.Partner'),
            preserve_default=False,
        ),
    ]
