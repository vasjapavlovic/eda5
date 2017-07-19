# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0004_auto_20170717_1728'),
        ('arhiv', '0002_arhiviranje_povprasevanje'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='razdelilnik',
            field=models.ForeignKey(null=True, to='razdelilnik.Razdelilnik', blank=True),
        ),
    ]
